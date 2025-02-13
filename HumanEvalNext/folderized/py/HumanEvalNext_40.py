from typing import List


def triples_sum_to_zero(l: List[int]) -> bool:
    """
    Check if there are three distinct elements
    in the list that sum to zero.

    Examples:
        >>> triples_sum_to_zero([1, 3, 5, 0])
        False
        >>> triples_sum_to_zero([1, 3, -2, 1])
        True
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False


def check(candidate):
    assert candidate([1, 3, 5, 0]) == False
    assert candidate([1, 3, 5, -1]) == False
    assert candidate([1, 3, -2, 1]) == True
    assert candidate([1, 2, 3, 7]) == False
    assert candidate([1, 2, 5, 7]) == False
    assert candidate([2, 4, -5, 3, 9, 7]) == True
    assert candidate([-5, 0, 5]) == True
    assert candidate([0, 0, 0]) == True
    assert candidate([0, 0]) == False
    assert candidate([1]) == False
    assert candidate([]) == False
    assert candidate([1, 3, 5, -100]) == False
    assert candidate([100, 3, 5, -100]) == False
    assert candidate([341, 101, -3, -98, 243]) == True


def test_check():
    check(triples_sum_to_zero)