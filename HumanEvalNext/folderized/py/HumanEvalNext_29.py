from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.
    
    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [x for x in strings if x.startswith(prefix)]


def check(candidate):
    assert candidate([], 'john') == []
    assert candidate(['john', 'jo', 'johnny'], 'john') == ['john', 'johnny']
    assert candidate(['a', '', ' ', 'bbb', '!C@'], '') == ['a', '', ' ', 'bbb', '!C@']
    assert candidate(['caps', 'CAPS', 'CaPs', 'cApS'], 'CAPS') == ['CAPS']
    assert candidate(['caps', 'CAPS', 'CaPs', 'cApS'], 'caps') == ['caps']
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']


def test_check():
    check(filter_by_prefix)