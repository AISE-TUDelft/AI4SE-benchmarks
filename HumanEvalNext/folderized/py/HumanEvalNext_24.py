def largest_divisor(n: int) -> int:
    """
    Find the largest number that divides n evenly, smaller than n.
    Return -1 if such a number does not exist.

    Example:
        >>> largest_divisor(15)
        5
    """
    if n <= 0:
        return -1
    for i in reversed(range(n)):
        if n % i == 0:
            return i


def check(candidate):
    assert candidate(3) == 1
    assert candidate(7) == 1
    assert candidate(10) == 5
    assert candidate(100) == 50
    assert candidate(49) == 7
    assert candidate(-4) == -1
    assert candidate(0) == -1


def test_check():
    check(largest_divisor)