def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return string.swapcase()


def check(candidate):
    assert candidate('') == ''
    assert candidate('Hello!') == 'hELLO!'
    assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'
    assert candidate('n\nN') == 'N\nn'
    assert candidate('    spa\tces    ') == '    SPA\tCES    '
    assert candidate('@#$%^&*()') == '@#$%^&*()'


def test_check():
    check(flip_case)