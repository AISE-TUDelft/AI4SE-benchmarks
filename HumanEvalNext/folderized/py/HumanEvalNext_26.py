from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all the elements that occur more than once.
    Keep the order of the elements the same as in the input.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 1, 1]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5]
    assert candidate([-1, -2, -3, -2, -4, -3, -5]) == [-1, -4, -5]
    assert candidate([1, -1]) == [1, -1]


def test_check():
    check(remove_duplicates)