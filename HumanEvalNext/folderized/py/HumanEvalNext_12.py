from typing import List


def longest(strings: List[str]) -> str:
    """
    Out of a list of strings, return the longest one.
    Return the first one in case of multiple strings of the same length.
    Return an empty string for edge cases.

    Examples:
        >>> longest(['a', 'b', 'c'])
        'a'
        >>> longest(['a', 'bb', 'ccc'])
        'ccc'
    """
    if not strings:
        return ''

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s


def check(candidate):
    assert candidate([]) == ''
    assert candidate(['x', 'y', 'z']) == 'x'
    assert candidate(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'
    assert candidate(['bb', 'aa']) == 'bb'
    assert candidate(['\n\n\n', 'n']) == '\n\n\n'
    assert candidate(['', '  n  ', 'nnn']) == '  n  '
    assert candidate(['five', '5']) == 'five'


def test_check():
    check(longest)