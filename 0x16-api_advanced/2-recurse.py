#!/usr/bin/python3
"""Contain a function that prints all hot titles in a subreddit"""

import requests


def recurse(subreddit, hot_list=[], counter=0, after=''):
    """Find all hotlists in a subreddit recursively"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after, 'count': counter}
    headers = {'User-Agent': "Mozilla/5.0"}
    resp = requests.get(url, params=params,
                        headers=headers, allow_redirects=False)
    try:
        posts = resp.json().get('data').get('children')
        counter += len(posts)
        after = resp.json().get('data').get('after')
        if after is None:
            raise AttributeError
        [hot_list.append(post['data']['title']) for post in posts]
    except (KeyError, AttributeError):
        return None if len(hot_list) == 0 else hot_list
    return recurse(subreddit, hot_list, counter, after)
