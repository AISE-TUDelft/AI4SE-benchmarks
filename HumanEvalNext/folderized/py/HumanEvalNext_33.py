from typing import List


def sort_third(l: List[int]) -> List[int]:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.

    Examples:
        >>> sort_third([1, 2, 3])
        [1, 2, 3]
        >>> sort_third([5, 6, 3, 4, 8, 9, 2])
        [2, 6, 3, 4, 8, 9, 5]
    """
    l = list(l)
    l[::3] = sorted(l[::3])
    return l


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3]) == [1, 2, 3]
    assert candidate([4, 2, 3, 1]) == [1, 2, 3, 4]
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]
    assert candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10]) == [-10, 8, -12, 3, 23, 2, 4, 11, 12, 5]
    assert candidate([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert candidate([5, 8, 3, 4, 6, 9, 2]) == [2, 8, 3, 4, 6, 9, 5]
    assert candidate([5, 6, 9, 4, 8, 3, 2]) == [2, 6, 9, 4, 8, 3, 5]
    assert candidate([5, 6, 3, 4, 8, 9, 2, 1]) == [2, 6, 3, 4, 8, 9, 5, 1]
    assert candidate([0, 8, -3, -7, 11, -11, 111, 5, 3, -6, 77, -77, 0]) == [-7, 8, -3, -6, 11, -11, 0, 5, 3, 0, 77, -77, 111]

def test_check():
    check(sort_third)