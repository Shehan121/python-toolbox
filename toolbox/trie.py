"""A prefix tree for fast prefix lookups."""


class Trie:
    """Store strings for prefix queries.

    >>> t = Trie()
    >>> t.insert("cat"); t.insert("car"); t.insert("dog")
    >>> t.contains("car")
    True
    >>> t.starts_with("ca")
    True
    >>> sorted(t.with_prefix("ca"))
    ['car', 'cat']
    """

    _END = object()

    def __init__(self):
        self._root = {}

    def insert(self, word):
        node = self._root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self._END] = True

    def _walk(self, prefix):
        node = self._root
        for ch in prefix:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def contains(self, word):
        node = self._walk(word)
        return node is not None and self._END in node

    def starts_with(self, prefix):
        return self._walk(prefix) is not None

    def with_prefix(self, prefix):
        """Yield every stored word beginning with *prefix*."""
        node = self._walk(prefix)
        if node is None:
            return
        stack = [(prefix, node)]
        while stack:
            text, cur = stack.pop()
            for key, child in cur.items():
                if key is self._END:
                    yield text
                else:
                    stack.append((text + key, child))
