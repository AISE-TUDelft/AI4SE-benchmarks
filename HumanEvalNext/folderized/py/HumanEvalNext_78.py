def hex_key(num: str) -> int:
    """
    Based on a hexadecimal number, received as a string,
    counts the number of hexadecimal digits that are primes.

    You may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.

    Examples:
        For num = "AB" the output should be 1.
        For num = "2020" the output should be 2.
    """
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total


def check(candidate):
    assert candidate("0") == 0
    assert candidate("AB") == 1
    assert candidate("1077E") == 2 
    assert candidate("ABED1A33") == 4     
    assert candidate("2020") == 2
    assert candidate("123456789ABCDEF0") == 6    
    assert candidate("112233445566778899AABBCCDDEEFF00") == 12
    assert candidate("") == 0


def test_check():
    check(hex_key)