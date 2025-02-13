from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    Return an empty list for any undefined edge cases.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(set(numbers)) < 2:
        return []
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]


def check(candidate):
    assert candidate([]) == []
    assert candidate([1.0]) == []
    assert candidate([1.0, 2.0]) == [0.0, 1.0]
    assert candidate([-4.0, -4.0, -4.0]) == []
    assert candidate([0.0, 0.0]) == []
    assert candidate([2.0, 49.9]) == [0.0, 1.0]
    assert candidate([100.0, 49.9]) == [1.0, 0.0]
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert candidate([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]
    assert candidate([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]
    assert candidate([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]
    assert candidate([-5.0, 0.0, 5.0]) == [0.0, 0.5, 1.0]
    assert candidate([-2.0, -1.0, 0.0, 1.0, 2.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert candidate([-5.0, -3.0, 0.0, 3.0, 5.0]) == [0.0, 0.2, 0.5, 0.8, 1.0]
    assert candidate([-20.0, -16.0, -14.0, -10.0]) == [0.0, 0.4, 0.6, 1.0]


def test_check():
    check(rescale_to_unit)