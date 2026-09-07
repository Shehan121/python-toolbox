"""In-place quicksort with a median-of-three pivot."""


def _median_of_three(seq, lo, hi):
    mid = (lo + hi) // 2
    a, b, c = seq[lo], seq[mid], seq[hi]
    if a > b:
        a, b = b, a
    if b > c:
        b = c
    return max(a, b)


def quicksort(seq):
    """Sort *seq* in place and return it.

    >>> quicksort([5, 2, 9, 1, 5, 6])
    [1, 2, 5, 5, 6, 9]
    >>> quicksort([])
    []
    """
    _qsort(seq, 0, len(seq) - 1)
    return seq


def _qsort(seq, lo, hi):
    while lo < hi:
        pivot = _median_of_three(seq, lo, hi)
        i, j = lo, hi
        while i <= j:
            while seq[i] < pivot:
                i += 1
            while seq[j] > pivot:
                j -= 1
            if i <= j:
                seq[i], seq[j] = seq[j], seq[i]
                i += 1
                j -= 1
        # Recurse into the smaller half to bound stack depth at O(log n).
        if j - lo < hi - i:
            _qsort(seq, lo, j)
            lo = i
        else:
            _qsort(seq, i, hi)
            hi = j
