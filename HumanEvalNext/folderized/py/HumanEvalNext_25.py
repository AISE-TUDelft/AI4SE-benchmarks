from typing import List


def factorize(n: int) -> List[int]:
    """
    Return a list of prime factors of the given integer in the order of smallest to largest.
    Each of the factors should be listed as often as it appears in the factorization.
    The input number should be equal to the product of all factors.

    Examples:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 5, 7]
    """
    assert n > 1
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact


def check(candidate):
    assert candidate(2) == [2]
    assert candidate(4) == [2, 2]
    assert candidate(8) == [2, 2, 2]
    assert candidate(57) == [3, 19]
    assert candidate(3249) == [3, 3, 19, 19]
    assert candidate(185193) == [3, 3, 3, 19, 19, 19]
    assert candidate(20577) == [3, 19, 19, 19]
    assert candidate(18) == [2, 3, 3]


def test_check():
    check(factorize)