from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Example:
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result


def check(candidate):
    assert candidate([], 7) == []
    assert candidate([1], 1) == [1]
    assert candidate([1, 3], 2) == [1, 2, 3]
    assert candidate([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]
    assert candidate([2, 2, 2], 2) == [2, 2, 2, 2, 2]
    assert candidate([0, 0, 0, 0, 0], 0) == [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate([-1, -2, -3], -4) == [-1, -4, -2, -4, -3]


def test_check():
    check(intersperse)