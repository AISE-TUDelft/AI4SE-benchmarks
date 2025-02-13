def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b:
        a, b = b, a % b
    return abs(a)


def check(candidate):
    assert candidate(3, 7) == 1
    assert candidate(10, 15) == 5
    assert candidate(49, 14) == 7
    assert candidate(144, 60) == 12
    assert candidate(8, 0) == 8
    assert candidate(0, -4) == 4
    assert candidate(-5, -10) == 5
    assert candidate(-2, 9) == 1


def test_check():
    check(greatest_common_divisor)