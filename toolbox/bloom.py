"""A compact Bloom filter."""

import hashlib
import math


class BloomFilter:
    """Probabilistic set membership with no false negatives.

    >>> bf = BloomFilter(capacity=1000, error_rate=0.01)
    >>> bf.add("hello")
    >>> "hello" in bf
    True
    >>> "goodbye" in bf
    False
    """

    def __init__(self, capacity=1000, error_rate=0.01):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        if not 0 < error_rate < 1:
            raise ValueError("error_rate must be between 0 and 1")
        self.capacity = capacity
        self.error_rate = error_rate
        self.size = max(1, int(-capacity * math.log(error_rate) / math.log(2) ** 2))
        self.hashes = max(1, round(self.size / capacity * math.log(2)))
        self._bits = bytearray((self.size + 7) // 8)
        self.count = 0

    def _positions(self, item):
        digest = hashlib.sha256(str(item).encode()).digest()
        h1 = int.from_bytes(digest[:8], "big")
        h2 = int.from_bytes(digest[8:16], "big") | 1
        for i in range(self.hashes):
            yield (h1 + i * h2) % self.size

    def add(self, item):
        for pos in self._positions(item):
            self._bits[pos // 8] |= 1 << (pos % 8)
        self.count += 1

    def __contains__(self, item):
        return all(
            self._bits[pos // 8] >> (pos % 8) & 1
            for pos in self._positions(item)
        )

    def __len__(self):
        return self.count
