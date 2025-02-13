from typing import List


def get_positive(l: List[int]) -> List[int]:
    """
    Return only the positive numbers in the list.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
    """
    return [e for e in l if e > 0]


def check(candidate):
    assert candidate([-1, -2, 4, 5, 6]) == [4, 5, 6]
    assert candidate([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 3, 9, 123, 1]
    assert candidate([-1, -2]) == []
    assert candidate([0]) == []
    assert candidate([]) == []
    assert candidate([2, 2, 2]) == [2, 2, 2]


def test_check():
    check(get_positive)