"""Disjoint-set union with path compression and union by rank."""


class UnionFind:
    """Track a partition of hashable items into disjoint sets.

    >>> uf = UnionFind()
    >>> uf.union("a", "b"); uf.union("b", "c")
    >>> uf.connected("a", "c")
    True
    >>> uf.connected("a", "z")
    False
    """

    def __init__(self):
        self._parent = {}
        self._rank = {}

    def find(self, item):
        if item not in self._parent:
            self._parent[item] = item
            self._rank[item] = 0
            return item
        root = item
        while self._parent[root] != root:
            root = self._parent[root]
        while self._parent[item] != root:
            self._parent[item], item = root, self._parent[item]
        return root

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self._rank[ra] < self._rank[rb]:
            ra, rb = rb, ra
        self._parent[rb] = ra
        if self._rank[ra] == self._rank[rb]:
            self._rank[ra] += 1

    def connected(self, a, b):
        return self.find(a) == self.find(b)
