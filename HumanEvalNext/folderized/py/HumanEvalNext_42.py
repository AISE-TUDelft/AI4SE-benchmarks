from typing import List


def incr_list(l: List[int]) -> List[int]:
    """
    Increment all elements of the list by 1.
    
    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
    """
    return [(e + 1) for e in l]


def check(candidate):
    assert candidate([]) == []
    assert candidate([3, 2, 1]) == [4, 3, 2]
    assert candidate([5, 2, 5, 2, 3, 3, 9, 0, 123]) == [6, 3, 6, 3, 4, 4, 10, 1, 124]
    assert candidate([1, 0, -1, -2, -3]) == [2, 1, 0, -1, -2]


def test_check():
    check(incr_list)