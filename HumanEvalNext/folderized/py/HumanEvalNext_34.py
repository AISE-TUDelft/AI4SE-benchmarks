from typing import List


def unique(l: List[int]) -> List[int]:
    """
    Return sorted unique elements in a list.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))


def check(candidate):
    assert candidate([]) == []
    assert candidate([2, 1, 2, 1, 2]) == [1, 2]
    assert candidate([-3, -2, -4, -2, -2, -3, -4]) == [-4, -3, -2]
    assert candidate([1, 2, 3]) == [1, 2, 3]
    assert candidate([0, 0, -1, 0, 1, 0, 1]) == [-1, 0, 1]
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]


def test_check():
    check(unique)