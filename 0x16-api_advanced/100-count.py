#!/usr/bin/python3
""" Reddit API"""

import requests

def count_words(subreddit, word_list, after=None, count=None):
    """Count occurrences of words in subreddit titles"""
    if after is None:
        count = {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}
    headers = {'user-agent': 'bhalut'}
    try:
        response = requests.get(url, params=params, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raises an error for bad response
        data = response.json()['data']
        for child in data['children']:
            title_words = child['data']['title'].lower().split()
            for word in word_list:
                if word.lower() in title_words:
                    count[word] = count.get(word, 0) + 1
        after = data.get('after')
        if after is None:
            for word, count_ in sorted(count.items(), key=lambda x: (-x[1], x[0])):
                print(f"{word}: {count_}")
        else:
            count_words(subreddit, word_list, after, count)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
