"""Run-length encoding for strings."""


def encode(text):
    """Compress runs of repeated characters.

    >>> encode("aaabbc")
    'a3b2c1'
    >>> encode("")
    ''
    """
    if not text:
        return ""
    out = []
    current = text[0]
    count = 1
    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            out.append(f"{current}{count}")
            current, count = ch, 1
    out.append(f"{current}{count}")
    return "".join(out)


def decode(encoded):
    """Expand a string produced by :func:`encode`.

    >>> decode("a3b2c1")
    'aaabbc'
    """
    out = []
    i = 0
    while i < len(encoded):
        ch = encoded[i]
        i += 1
        digits = ""
        while i < len(encoded) and encoded[i].isdigit():
            digits += encoded[i]
            i += 1
        if not digits:
            raise ValueError(f"missing run length after {ch!r}")
        out.append(ch * int(digits))
    return "".join(out)
