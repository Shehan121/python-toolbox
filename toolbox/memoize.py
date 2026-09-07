"""Memoisation with an optional time-to-live."""

import functools
import time


def memoize(ttl=None):
    """Cache a function's return value per argument tuple.

    Arguments must be hashable. Pass *ttl* in seconds to expire entries.

    >>> calls = []
    >>> @memoize()
    ... def square(n):
    ...     calls.append(n)
    ...     return n * n
    >>> square(4), square(4)
    (16, 16)
    >>> calls
    [4]
    """
    def decorate(func):
        cache = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.monotonic()
            if key in cache:
                value, stored_at = cache[key]
                if ttl is None or now - stored_at < ttl:
                    return value
            value = func(*args, **kwargs)
            cache[key] = (value, now)
            return value

        wrapper.cache_clear = cache.clear
        wrapper.cache_size = lambda: len(cache)
        return wrapper
    return decorate
