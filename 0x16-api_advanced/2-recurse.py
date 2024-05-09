#!/usr/bin/python3
"""
Using Reddit's API
"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Return top ten post titles recursively from a subreddit.
    """
    if hot_list is None:
        hot_list = []

    user_agent = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, params=params, headers=user_agent, allow_redirects=False)
        response.raise_for_status()  # Raises an error for bad response

        data = response.json().get("data")
        after_data = data.get("after")

        if after_data:
            recurse(subreddit, hot_list, after=after_data)

        all_titles = data.get("children")
        for title_ in all_titles:
            hot_list.append(title_["data"]["title"])

        return hot_list

    except requests.RequestException:
        return None
