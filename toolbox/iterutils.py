"""Iterator helpers that avoid materialising whole sequences."""

from itertools import islice


def flatten(nested, depth=None):
    """Yield leaves of an arbitrarily *nested* iterable.

    Strings and bytes are treated as leaves, not as iterables.

    >>> list(flatten([1, [2, [3, [4]]]]))
    [1, 2, 3, 4]
    >>> list(flatten([1, [2, [3]]], depth=1))
    [1, 2, [3]]
    """
    for item in nested:
        atomic = isinstance(item, (str, bytes)) or not hasattr(item, "__iter__")
        if atomic or depth == 0:
            yield item
        else:
            yield from flatten(item, None if depth is None else depth - 1)


def chunked(iterable, size):
    """Yield lists of at most *size* items from *iterable*.

    >>> list(chunked(range(7), 3))
    [[0, 1, 2], [3, 4, 5], [6]]
    """
    if size <= 0:
        raise ValueError("size must be positive")
    it = iter(iterable)
    while True:
        chunk = list(islice(it, size))
        if not chunk:
            return
        yield chunk


def unique(iterable, key=None):
    """Yield items in order, skipping ones already seen.

    >>> list(unique([1, 2, 1, 3, 2]))
    [1, 2, 3]
    """
    seen = set()
    for item in iterable:
        marker = item if key is None else key(item)
        if marker not in seen:
            seen.add(marker)
            yield item
