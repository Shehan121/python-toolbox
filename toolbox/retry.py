"""A retry decorator with exponential backoff."""

import functools
import random
import time


def retry(attempts=3, delay=0.1, backoff=2.0, jitter=0.0, exceptions=(Exception,)):
    """Retry the wrapped callable when it raises one of *exceptions*.

    The final attempt's exception propagates unchanged, so callers still
    see the real failure rather than a wrapper error.

    >>> calls = []
    >>> @retry(attempts=3, delay=0)
    ... def flaky():
    ...     calls.append(1)
    ...     if len(calls) < 3:
    ...         raise ValueError("not yet")
    ...     return "ok"
    >>> flaky()
    'ok'
    >>> len(calls)
    3
    """
    if attempts < 1:
        raise ValueError("attempts must be at least 1")

    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            wait = delay
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == attempts:
                        raise
                    if wait:
                        time.sleep(wait + random.uniform(0, jitter))
                    wait *= backoff
        return wrapper
    return decorate
