from typing import List


def max_element(l: List[int]) -> int:
    """
    Return the maximum element in the list.
    Assume that the list is not empty.
    
    Example:
        >>> max_element([1, 2, 3])
        3
    """
    assert len(l) > 0
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m


def check(candidate):
    assert candidate([0]) == 0
    assert candidate([-3, -8, -21]) == -3
    assert candidate([1, 2, 3, 4, 0, 1, 2, 3]) == 4
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124
    assert candidate([4, 4, 4, 3, 3, 3, 5, 0, 2, 2]) == 5


def test_check():
    check(max_element)