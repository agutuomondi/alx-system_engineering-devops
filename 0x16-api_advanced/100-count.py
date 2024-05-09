#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""


import requests


def count_words(subreddit, word_list, after='', word_dict=None):
    """
    count all words
    """
    if word_dict is None:
        word_dict = {word.lower(): 0 for word in word_list}

    if after is None:
        word_dict_sorted = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in word_dict_sorted:
            if count:
                print('{}: {}'.format(word, count))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split()]
            for word in word_dict:
                word_dict[word] += lower.count(word)

    except Exception:
        return None

