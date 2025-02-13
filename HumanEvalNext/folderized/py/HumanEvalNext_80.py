def is_happy(s: str) -> bool:
    """
    Check if the string is happy or not:
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

    Examples:
      is_happy(a) => False
      is_happy(aa) => False
      is_happy(abcd) => True
      is_happy(aabb) => False
    """
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
            return False
    return True


def check(candidate):
    assert candidate("g") == False
    assert candidate("qq") == False
    assert candidate("pqrst") == True
    assert candidate("hello") == False
    assert candidate("adb") == True
    assert candidate("xyy") == False
    assert candidate("iopaxpoi") == True
    assert candidate("iopaxioi") == False


def test_check():
    check(is_happy)