from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    assert len(numbers) > 0
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0 / 3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0 / 5.0) < 1e-6
    assert abs(candidate([0.0, 0.0, 0.0]) - 0.0) < 1e-6
    assert abs(candidate([-1.0, 1.0]) - 1.0) < 1e-6
    assert abs(candidate([1.5, -2.5, 3.5]) - 20.0 / 9.0) < 1e-6
    assert abs(candidate([1e6, 2e6, 3e6]) - 1e6 * 2.0 / 3.0) < 1e-6
    assert abs(candidate([-0.1, 0.1, -0.2, 0.2]) - 0.15) < 1e-6
    assert abs(candidate([1.234, 2.345, 3.456]) - 0.74 - 2.0 / 3000.0) < 1e-6
    assert abs(candidate([0.0, 1.0, -1.0]) - 2.0/3.0) < 1e-6
    assert abs(candidate([1.0]) - 0.0) < 1e-6


def test_check():
    check(mean_absolute_deviation)