def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Example:
        >>> how_many_times('aaaa', 'aa')
        3
    """
    times = 0

    if not substring:
        return len(string) + 1

    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            times += 1

    return times


def check(candidate):
    assert candidate('', 'x') == 0
    assert candidate('xyxyxyx', 'x') == 4
    assert candidate('cacacacac', 'cac') == 4
    assert candidate('john doe', 'john') == 1
    assert candidate('1  2 324 5', ' 2') == 1
    assert candidate('xy', 'xyz') == 0
    assert candidate('abc', '') == 4
    assert candidate('n\nn', 'n') == 2
    assert candidate('\n\n', '') == 3
    assert candidate('.oO0().oO0()', 'O') == 2
    assert candidate('aaa\naaa\naaa', 'aaa') == 3


def test_check():
    check(how_many_times)