from typing import List


def below_threshold(l: List[int], t: int) -> bool:
    """
    Check if all numbers in the list l are below threshold t.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    for e in l:
        if e >= t:
            return False
    return True


def check(candidate):
    assert candidate([1, 2, 4, 10], 100) == True
    assert candidate([1, 20, 4, 10], 5) == False
    assert candidate([1, 20, 4, 10], 21) == True
    assert candidate([1, 20, 4, 10], 22) == True
    assert candidate([1, 8, 4, 10], 11) == True
    assert candidate([1, 8, 4, 10], 10) == False
    assert candidate([-1, -2, -4, -10], -100) == False
    assert candidate([-1, -2, -4, -10], 0) == True


def test_check():
    check(below_threshold)