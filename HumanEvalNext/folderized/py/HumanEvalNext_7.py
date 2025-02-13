from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Example:
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [x for x in strings if substring in x]


def check(candidate):
    assert candidate([], 'john') == []
    assert candidate([], '') == []
    assert candidate(['', ' ', '   '], ' ') == [' ', '   ']
    assert candidate(['jo'], 'john') == []
    assert candidate(['john'], 'john') == ['john']
    assert candidate(['JOHN'], 'john') == []
    assert candidate(['jo hn', 'jo', 'hn'], 'john') == []
    assert candidate(['', 'a', 'aa'], '') == ['', 'a', 'aa']
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']
    assert candidate(['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx') == ['xxx', 'aaaxxy', 'xxxAAA', 'xxx']
    assert candidate(['grunt', 'trumpet', 'prune', 'gruesome'], 'run') == ['grunt', 'prune']
    assert candidate(['n\nn', 'nn', 'n\tn'], 'nn') == ['nn']
    assert candidate(['n\nn', 'nn', 'n\tn'], '\n') == ['n\nn']


def test_check():
    check(filter_by_substring)