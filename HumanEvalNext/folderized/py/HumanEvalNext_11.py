from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Example:
        >>> string_xor('10', '110')
        '100'
    """
    if len(a) < len(b):
        a = '0' * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = '0' * (len(a) - len(b)) + b

    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0', '0') == '0'
    assert candidate('1', '0') == '1'
    assert candidate('0', '1') == '1'
    assert candidate('0101', '0000') == '0101'
    assert candidate('', '101') == '101'
    assert candidate('101', '') == '101'
    assert candidate('', '') == ''
    assert candidate('1110101', '1010') == '1111111'


def test_check():
    check(string_xor)