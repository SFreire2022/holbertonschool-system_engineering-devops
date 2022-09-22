#!/usr/bin/python3
"""
How many subs?
"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "linux:Custom User Agent for Redit API"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
