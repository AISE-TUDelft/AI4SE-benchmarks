def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('car')
        False
    """
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True


def check(candidate):
    assert candidate('') == True
    assert candidate('aba') == True
    assert candidate('aaaaa') == True
    assert candidate('zbcd') == False
    assert candidate('xywyx') == True
    assert candidate('xywyz') == False
    assert candidate('xywzx') == False
    assert candidate('palindrome') == False
    assert candidate('12321') == True
    assert candidate('n\nn') == True
    assert candidate('t\tt') == True


def test_check():
    check(is_palindrome)