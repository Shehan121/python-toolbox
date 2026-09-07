"""Binary search over a sorted sequence."""


def binary_search(seq, target):
    """Return the index of *target* in sorted *seq*, or -1 if absent.

    >>> binary_search([1, 3, 5, 7, 9], 7)
    3
    >>> binary_search([1, 3, 5, 7, 9], 4)
    -1
    """
    lo, hi = 0, len(seq) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if seq[mid] == target:
            return mid
        if seq[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def bisect_left(seq, target):
    """Return the leftmost insertion point for *target* in sorted *seq*.

    >>> bisect_left([1, 2, 2, 2, 3], 2)
    1
    """
    lo, hi = 0, len(seq)
    while lo < hi:
        mid = (lo + hi) // 2
        if seq[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
