def circular_shift(x: int, shift: int) -> str:
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Examples:
        >>> circular_shift(12, 1)
        "21"
        >>> circular_shift(12, 2)
        "12"
    """
    s = str(x)
    if shift > len(s):
        return s[::-1]

    shift = shift % len(s)
    return s[len(s) - shift:] + s[:len(s) - shift]


def check(candidate):
    assert candidate(100, 2) == "001"
    assert candidate(12, 2) == "12"
    assert candidate(97, 8) == "79"
    assert candidate(12, 1) == "21"
    assert candidate(10, 101) == "01"
    assert candidate(123, 0) == "123"
    assert candidate(123, 2) == "231"
    assert candidate(123, 3) == "123"
    assert candidate(123, -2) == "312"
    assert candidate(456, -5) == "645"
    assert candidate(53124, -8) == "24531"
    assert candidate(1, -10000) == "1"


def test_check():
    check(circular_shift)