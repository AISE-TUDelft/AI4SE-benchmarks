from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Example:
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)


def check(candidate):
    assert candidate([]) == ''
    assert candidate(['', '', '']) == ''
    assert candidate(['x', 'yy', 'zzz']) == 'xyyzzz'
    assert candidate(['x', 'y', 'z,', 'w', 'k!']) == 'xyz,wk!'
    assert candidate(['\n', '\t', ' ']) == '\n\t '
    assert candidate(['\"', 'string', '\"']) == '\"string\"'


def test_check():
    check(concatenate)