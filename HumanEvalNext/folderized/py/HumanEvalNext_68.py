from typing import List


def pluck(arr: List[int]) -> List[int]:
    """
    Given an array representing a branch of a tree that has integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smallest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []

    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.
    """
    if (len(arr) == 0):
        return []

    evens = list(filter(lambda x: x % 2 == 0, arr))
    if (evens == []):
        return []

    return [min(evens), arr.index(min(evens))]


def check(candidate):
    assert candidate([4, 2, 3]) == [2, 1]
    assert candidate([1, 2, 3]) == [2, 1]
    assert candidate([]) == []
    assert candidate([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert candidate([1, 2, 3, 0, 5, 3]) == [0, 3]
    assert candidate([5, 4, 8, 4, 8]) == [4, 1]
    assert candidate([1, 6, 7, 1, 6]) == [6, 1]
    assert candidate([7, 9, 7, 1]) == []
    assert candidate([-1, -2, -3, -4, -5]) == [-4, 3]
    assert candidate([5, -13, 4, 71, -98, 0, -5, 186, -1, 5, 109, -239, 4]) == [-98, 4]
    assert candidate([1, -1, 2, -2, 3, -3, 2, -2, 1, -1]) == [-2, 3]


def test_check():
    check(pluck)