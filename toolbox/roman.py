"""Convert between integers and Roman numerals."""

_VALUES = (
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
)

_SYMBOLS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(number):
    """Return the Roman numeral for *number* (1-3999).

    >>> to_roman(1994)
    'MCMXCIV'
    >>> to_roman(4)
    'IV'
    """
    if not 1 <= number <= 3999:
        raise ValueError("number must be between 1 and 3999")
    parts = []
    for value, symbol in _VALUES:
        count, number = divmod(number, value)
        parts.append(symbol * count)
    return "".join(parts)


def from_roman(numeral):
    """Return the integer value of a Roman *numeral*.

    >>> from_roman("MCMXCIV")
    1994
    """
    total = 0
    previous = 0
    for ch in reversed(numeral.upper()):
        value = _SYMBOLS[ch]
        total += -value if value < previous else value
        previous = max(previous, value)
    return total
