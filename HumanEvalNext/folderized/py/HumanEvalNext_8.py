from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Example:
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value


def check(candidate):
    assert candidate([]) == (0, 1)
    assert candidate([1, 1, 1]) == (3, 1)
    assert candidate([100, 0]) == (100, 0)
    assert candidate([3, 5, 7]) == (15, 105)
    assert candidate([10]) == (10, 10)
    assert candidate([-1, -2, -3]) == (-6, -6)
    assert candidate([0, 0, 0]) == (0, 0)
    assert candidate([-1, 1, -1, 1]) == (0, 1)
    assert candidate([48, 57, 61, -19, -32]) == (115, 101472768)


def test_check():
    check(sum_product)