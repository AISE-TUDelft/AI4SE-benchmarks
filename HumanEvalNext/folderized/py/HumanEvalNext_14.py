from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result


def check(candidate):
    assert candidate('') == []
    assert candidate(' a ') == [' ', ' a', ' a ']
    assert candidate('abc\nde\tf') == ['a', 'ab', 'abc', 'abc\n', 'abc\nd', 'abc\nde', 'abc\nde\t', 'abc\nde\tf']
    assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
    assert candidate('WWW') == ['W', 'WW', 'WWW']
    assert candidate('00101') == ['0', '00', '001', '0010', '00101']


def test_check():
    check(all_prefixes)