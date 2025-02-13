from typing import List


def filter_integers(values: List[str]) -> List[int]:
    """
    Filter given list of string values only for integers.

    Example:
        >>> filter_integers(['10', ' 123 ', '5.0', three', 'abc', '{}'])
        [10]
    """
    return [int(x) for x in values if x.isdigit()]


def check(candidate):
    assert candidate([]) == []
    assert candidate(['4', '{}', '[1]', '23.2', '9', 'adasd']) == [4, 9]
    assert candidate(['3', 'c', '3', '3', 'a', 'b']) == [3, 3, 3]
    assert candidate(['0', '1', 'O', 'o', 'False', '1e5']) == [0, 1]
    assert candidate(['10-8', '10 - 8', '4*2', '4 / 2', '4+2', '3**8', '4 % 2', '1!', '1.f']) == []
    assert candidate(['', '3 ', ' 3', ' 3 ']) == []
    assert candidate(['10', ' 123 ', '5.0', 'three', 'abc', '{}']) == [10]
    assert candidate(['0', '1', 'O', 'o', 'False', '5678', '1e5']) == [0, 1, 5678]


def test_check():
    check(filter_integers)