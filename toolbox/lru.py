"""A fixed-capacity LRU cache built on an ordered dict."""

from collections import OrderedDict


class LRUCache:
    """Least-recently-used cache with O(1) get and put.

    >>> c = LRUCache(2)
    >>> c.put("a", 1); c.put("b", 2); c.get("a")
    1
    >>> c.put("c", 3)          # evicts "b", the least recently used
    >>> c.get("b") is None
    True
    """

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._data = OrderedDict()

    def get(self, key, default=None):
        if key not in self._data:
            return default
        self._data.move_to_end(key)
        return self._data[key]

    def put(self, key, value):
        if key in self._data:
            self._data.move_to_end(key)
        self._data[key] = value
        if len(self._data) > self.capacity:
            self._data.popitem(last=False)

    def __len__(self):
        return len(self._data)

    def __contains__(self, key):
        return key in self._data
