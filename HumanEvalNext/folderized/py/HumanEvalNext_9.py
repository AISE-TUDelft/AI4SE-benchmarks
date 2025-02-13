from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found
    until given moment in the sequence.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result


def check(candidate):
    assert candidate([]) == []
    assert candidate([-1]) == [-1]
    assert candidate([0, 1, 2, 3, 4]) == [0, 1, 2, 3, 4]
    assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]
    assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]
    assert candidate([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert candidate([1, 0, -1, 2]) == [1, 1, 1, 2]
    assert candidate([10, 20, 30, 40, 30, 20, 10]) == [10, 20, 30, 40, 40, 40, 40]
    assert candidate([0, 0, -1, 0, 0]) == [0, 0, 0, 0, 0]
    assert candidate([-2, -4, -1, -5]) == [-2, -2, -1, -1]

def test_check():
    check(rolling_max)