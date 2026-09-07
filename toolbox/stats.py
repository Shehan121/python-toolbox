"""Descriptive statistics without a numeric dependency."""

import math


def mean(values):
    """Return the arithmetic mean.

    >>> mean([1, 2, 3, 4])
    2.5
    """
    values = list(values)
    if not values:
        raise ValueError("mean requires at least one value")
    return sum(values) / len(values)


def median(values):
    """Return the middle value, averaging the two middles when even.

    >>> median([3, 1, 2])
    2
    >>> median([4, 1, 3, 2])
    2.5
    """
    ordered = sorted(values)
    n = len(ordered)
    if n == 0:
        raise ValueError("median requires at least one value")
    mid = n // 2
    if n % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def stdev(values, population=False):
    """Return the standard deviation.

    Defaults to the sample (n-1) estimator; pass ``population=True``
    for the n divisor.

    >>> round(stdev([2, 4, 4, 4, 5, 5, 7, 9], population=True), 4)
    2.0
    """
    values = list(values)
    n = len(values)
    divisor = n if population else n - 1
    if divisor < 1:
        raise ValueError("not enough values for the requested estimator")
    mu = mean(values)
    return math.sqrt(sum((v - mu) ** 2 for v in values) / divisor)


def percentile(values, p):
    """Return the *p*-th percentile (0-100) using linear interpolation.

    >>> percentile([1, 2, 3, 4], 50)
    2.5
    """
    if not 0 <= p <= 100:
        raise ValueError("p must be between 0 and 100")
    ordered = sorted(values)
    if not ordered:
        raise ValueError("percentile requires at least one value")
    pos = (len(ordered) - 1) * p / 100
    low = math.floor(pos)
    high = math.ceil(pos)
    if low == high:
        return ordered[low]
    return ordered[low] + (ordered[high] - ordered[low]) * (pos - low)
