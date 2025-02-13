def is_prime(n: int) -> bool:
    """
    Check if given number is considered to be prime.

    Examples:
        >>> is_prime(6)
        False
        >>> is_prime(100)
        False
        >>> is_prime(11)
        True
    """
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True


def check(candidate):
    assert candidate(-5) == False
    assert candidate(-1) == False
    assert candidate(0) == False
    assert candidate(1) == False
    assert candidate(2) == True
    assert candidate(3) == True
    assert candidate(4) == False
    assert candidate(5) == True
    assert candidate(6) == False
    assert candidate(101) == True
    assert candidate(11) == True
    assert candidate(13441) == True
    assert candidate(61) == True
    assert candidate(4) == False
    assert candidate(1) == False
    assert candidate(5) == True
    assert candidate(11) == True
    assert candidate(17) == True
    assert candidate(85) == False
    assert candidate(77) == False
    assert candidate(255379) == False
    assert candidate(999331) == True


def test_check():
    check(is_prime)