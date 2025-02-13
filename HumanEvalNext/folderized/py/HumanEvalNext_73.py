from typing import List


def smallest_change(arr: List[int]) -> int:
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
        smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
        smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
        smallest_change([1, 2, 3, 2, 1]) == 0
    """
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans


def check(candidate):
    assert candidate([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    assert candidate([1, 11, 111, 1111, 1, 11]) == 3
    assert candidate([1, 2, 3, 4, 3, 2, 2]) == 1
    assert candidate([1, 4, 2]) == 1
    assert candidate([1, 4, 4, 2]) == 1
    assert candidate([1, 2, 3, 2, 1]) == 0
    assert candidate([3, 1, 1, 3]) == 0
    assert candidate([-1, -11, 1]) == 1
    assert candidate([-4, 2, 4, -2]) == 2
    assert candidate([1]) == 0
    assert candidate([]) == 0
    assert candidate([0, 1]) == 1


def test_check():
    check(smallest_change)