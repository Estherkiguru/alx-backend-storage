#!/usr/bin/env python3
"""
Caching request and tracking module
"""
import redis
import requests
from functools import wraps
from typing import Callable


def track_get_page(fn: Callable) -> Callable:
    """get_page decorator
    """
    @wraps(fn)
    def wrapper(url: str) -> str:
        """ Wrapper that checks whether a url's data is cached
        """
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(url)
        client.set(f'{url}', response, 10)
        return response
    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """ Makes a http request
    Returns:content of URL after caching the requests
    """
    response = requests.get(url)
    return response.text