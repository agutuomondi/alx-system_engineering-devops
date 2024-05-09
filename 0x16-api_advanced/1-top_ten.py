#!/usr/bin/python3

"""
Prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    headers = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raises an error for bad response
        data = response.json()
        
        for post in data['data']['children']:
            print(post['data']['title'])

    except (requests.RequestException, KeyError):
        print("None")

