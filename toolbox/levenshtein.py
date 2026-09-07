"""Edit distance between two strings."""


def levenshtein(a, b):
    """Return the Levenshtein distance between *a* and *b*.

    Uses a rolling row, so memory is O(min(len(a), len(b))).

    >>> levenshtein("kitten", "sitting")
    3
    >>> levenshtein("", "abc")
    3
    >>> levenshtein("same", "same")
    0
    """
    if len(a) < len(b):
        a, b = b, a
    if not b:
        return len(a)

    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        current = [i]
        for j, cb in enumerate(b, start=1):
            current.append(min(
                previous[j] + 1,          # deletion
                current[j - 1] + 1,       # insertion
                previous[j - 1] + (ca != cb),  # substitution
            ))
        previous = current
    return previous[-1]


def similarity(a, b):
    """Return a 0.0-1.0 similarity ratio derived from the edit distance.

    >>> similarity("abc", "abc")
    1.0
    """
    longest = max(len(a), len(b))
    if longest == 0:
        return 1.0
    return 1.0 - levenshtein(a, b) / longest
