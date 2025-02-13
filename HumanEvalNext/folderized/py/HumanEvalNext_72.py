from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    """
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.
    If the requirements are not met, the object will not fly.
    
    Other requirements:
        * w is a non-negative integer
        * q is a list of non-negative integers
        * q is a connected object, i.e. no zeros between non-zero elements

    Examples:
        will_it_fly([1, 2], 5) == False 
        (1 + 2 is less than the maximum possible weight, but it's unbalanced)

        will_it_fly([3, 2, 3], 1) == False
        (it's balanced, but 3 + 2 + 3 is more than the maximum possible weight)

        will_it_fly([3, 2, 3], 9) == True
        (3 + 2 + 3 is less than the maximum possible weight, and it's balanced)

        will_it_fly([0, 3], 5) == True
        (3 is less than the maximum possible weight, and it's balanced since the 0 is negligible for the balance)
    """
    if w < 0:
        # Invalid weight
        return False

    if sum(q) > w:
        # Too heavy
        return False
    
    if len(q) == 0 or sum(q) <= 0:
        # Nothing to fly
        return False
    
    if any([x < 0 for x in q]):
        # Negative elements
        return False
    
    # Remove leading and trailing zeros
    while q and q[0] == 0:
        q.pop(0)
    while q and q[-1] == 0:
        q.pop(-1)
    if len(q) == 0 or 0 in q:
        # Invalid object
        return False

    i, j = 0, len(q) - 1
    while i < j:
        if q[i] != q[j]:
            # Unbalanced
            return False
        i += 1
        j -= 1
    return True


def check(candidate):
    assert candidate([1, 1, 1], 3) == True
    assert candidate([1], 0) == False
    assert candidate([3, 2, 3], 9) == True
    assert candidate([1, 2], 5) == False
    assert candidate([3], 5) == True
    assert candidate([3, 2, 3], 1) == False
    assert candidate([1, 2, 3], 6) == False
    assert candidate([5], 5) == True
    assert candidate([0, 1, 6, 5, 6, 1, 0], 20) == True
    assert candidate([], 10) == False
    assert candidate([], 0) == False
    assert candidate([0], 10) == False
    assert candidate([0, 0, 0, 8], 10) == True
    assert candidate([0, 0, 0, 0, 3, 1, 4, 1, 3, 0], 50) == True
    assert candidate([0, 0, 0, 1, 4, 0, 4, 1, 0, 0], 12) == False
    assert candidate([9, 0, 0, 0, 0, 0, 0], 9) == True
    assert candidate([0, 0, 4, 2, 4, 0, 0, 0, 0, -1, 0], 100) == False
    assert candidate([4, -2, 4], 6) == False
    assert candidate([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 100) == False
    assert candidate([0], -5) == False
    assert candidate([-1], 1) == False


def test_check():
    check(will_it_fly)