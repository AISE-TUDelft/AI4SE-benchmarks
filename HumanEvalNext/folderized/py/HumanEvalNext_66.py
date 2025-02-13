def digitSum(s: str) -> int:
    """
    Take a string as input and return the sum of the the ASCII codes from upper characters only.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    if s == "":
        return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)


def check(candidate):
    assert candidate("") == 0
    assert candidate("abAB\nabAB") == 262
    assert candidate("ab_AB") == 131
    assert candidate("abcCd") == 67
    assert candidate("hel!loE") == 69
    assert candidate("woArBld") == 131
    assert candidate("aAaaaXa") == 153
    assert candidate(" How are yOu?") == 151
    assert candidate("Y0u arE Very Smart  ") == 327


def test_check():
    check(digitSum)