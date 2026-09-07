"""Prime generation and factorisation."""


def primes_below(limit):
    """Return every prime strictly below *limit*.

    >>> primes_below(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> primes_below(2)
    []
    """
    if limit <= 2:
        return []
    flags = bytearray([1]) * limit
    flags[0] = flags[1] = 0
    for n in range(2, int(limit ** 0.5) + 1):
        if flags[n]:
            flags[n * n::n] = bytearray(len(range(n * n, limit, n)))
    return [n for n in range(limit) if flags[n]]


def factorise(n):
    """Return the prime factors of *n* in ascending order.

    >>> factorise(360)
    [2, 2, 2, 3, 3, 5]
    """
    if n < 2:
        return []
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1 if divisor == 2 else 2
    if n > 1:
        factors.append(n)
    return factors
