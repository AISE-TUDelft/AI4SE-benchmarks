def vowels_count(s: str) -> int:
    """
    Write a function vowels_count which takes a string representing
    a single word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word. Note, trailing
    special characters or spaces do not matter, however, numbers and letters do effect
    whether 'y' is considered to be the last letter of the word.

    Examples:
        >>> vowels_count("abcde")
        2
        >>> vowels_count(" ACEDY!")
        3
    """
    assert " " not in s.strip()  # input is a single word

    import re
    if len(re.sub(r'[^aeiouyAEIOUY]', '', s)) == 0:
        return 0

    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)

    last_vowel = re.sub(r'[^a-zA-Z0-9]', '', s)
    if last_vowel[-1] == 'y' or last_vowel[-1] == 'Y':
        n_vowels += 1

    return n_vowels


def check(candidate):
    assert candidate("") == 0
    assert candidate("abcde") == 2
    assert candidate("AlOne") == 3
    assert candidate("key") == 2
    assert candidate("bye") == 1
    assert candidate("keY") == 2
    assert candidate("bYe") == 1
    assert candidate("yy") == 1
    assert candidate("ACEDY") == 3
    assert candidate("BY3") == 0
    assert candidate("mrkLnvYpq") == 0
    assert candidate("aeiouAEIOU\ny") == 11
    assert candidate("  key  ") == 2
    assert candidate("KeY.") == 2


def test_check():
    check(vowels_count)