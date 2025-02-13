def iscube(a: int) -> bool:
    """
    Check if number a is a cube of some integer number.
    
    Examples:
        iscube(2) == False
        iscube(64) == True
        iscube(-180) == False
    """
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a


def check(candidate):

    # Check some simple cases
    assert candidate(0) == True
    assert candidate(1) == True
    assert candidate(2) == False
    assert candidate(-1) == True
    assert candidate(64) == True
    assert candidate(180) == False
    assert candidate(1000) == True
    assert candidate(29791) == True
    assert candidate(-2197) == True
    assert candidate(1729) == False
    assert candidate(-9827643) == False
    assert candidate(9800481) == False


def test_check():
    check(iscube)