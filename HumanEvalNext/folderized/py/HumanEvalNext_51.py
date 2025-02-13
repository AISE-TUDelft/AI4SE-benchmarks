def remove_vowels(text: str) -> str:
    """
    Return the text without vowels (a, e, i, o, u).

    Examples:
        >>> remove_vowels('abcdef')
        'bcdf'
        >>> remove_vowels('aaaaa')
        ''
        >>> remove_vowels('aaBAA')
        'B'
        >>> remove_vowels('zbcd')
        'zbcd'
    """
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])


def check(candidate):
    assert candidate('') == ''
    assert candidate("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert candidate('abc\tdef') == 'bc\tdf'
    assert candidate('fedcba') == 'fdcb'
    assert candidate('eeeee') == ''
    assert candidate('acBAA') == 'cB'
    assert candidate('EcBOO') == 'cB'
    assert candidate('ybcd') == 'ybcd'
    assert candidate('1a2b3c4d5e') == '12b3c4d5'
    assert candidate('  spac e s ') == '  spc  s '
    assert candidate('!@#a$E%^u&*()') == '!@#$%^&*()'


def test_check():
    check(remove_vowels)