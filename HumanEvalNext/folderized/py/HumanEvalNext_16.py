def count_distinct_characters(string: str) -> int:
    """
    Find out how many distinct characters (regardless of case) are in the string.

    Examples:
        >>> count_distinct_characters("xyzXYZ")
        3
        >>> count_distinct_characters("Jerry")
        4
    """
    return len(set(string.lower()))


def check(candidate):
    assert candidate("") == 0
    assert candidate("abcde") == 5
    assert candidate("abcdecadeCADE") == 5
    assert candidate("aaaaAAAAaaaa") == 1
    assert candidate("Jerry jERRY JeRRRY") == 5
    assert candidate('                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ') == 1
    assert candidate('f[]F{}f[]F{}f[]F{}f[]F{}f[]F{}') == 5
    assert candidate('\t\t\t\t\t\t\t\t\t\t') == 1
    assert candidate("!%@#&($^!%^&@*())@)") == 10


def test_check():
    check(count_distinct_characters)