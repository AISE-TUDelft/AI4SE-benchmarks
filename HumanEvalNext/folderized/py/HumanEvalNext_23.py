def strlen(string: str) -> int:
    """
    Return the length of the given string.
    
    Example:
        >>> strlen('abc')
        3
    """
    return len(string)


def check(candidate):
    assert candidate('') == 0
    assert candidate(' ') == 1
    assert candidate('x') == 1
    assert candidate('asdasnakj') == 9
    assert candidate('    s   p a   c   e s  ') == 23
    assert candidate('a\nb\tc') == 5
    assert candidate('False') == 5
    assert candidate('10') == 2
    assert candidate('\"') == 1


def test_check():
    check(strlen)