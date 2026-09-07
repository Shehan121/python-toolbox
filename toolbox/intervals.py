"""Operations on closed numeric intervals."""


def merge(intervals):
    """Merge overlapping or touching intervals.

    >>> merge([(1, 3), (2, 6), (8, 10), (15, 18)])
    [(1, 6), (8, 10), (15, 18)]
    >>> merge([])
    []
    """
    ordered = sorted(intervals)
    merged = []
    for start, end in ordered:
        if start > end:
            raise ValueError(f"interval ({start}, {end}) is reversed")
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged


def intersect(a, b):
    """Return the overlap of two intervals, or None.

    >>> intersect((1, 5), (3, 8))
    (3, 5)
    >>> intersect((1, 2), (5, 6)) is None
    True
    """
    start = max(a[0], b[0])
    end = min(a[1], b[1])
    return (start, end) if start <= end else None


def total_length(intervals):
    """Return the measure of the union of *intervals*.

    >>> total_length([(1, 3), (2, 6)])
    5
    """
    return sum(end - start for start, end in merge(intervals))
