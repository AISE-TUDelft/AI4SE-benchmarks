def decimal_to_binary(decimal: int) -> str:
    """
    You will be given a number in decimal form (decimal system).
    Convert it to binary format and return it as a string.
    You may assume the input is positive.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Example:
        decimal_to_binary(15) == "db1111db"
    """
    assert decimal >= 0
    return "db" + bin(decimal)[2:] + "db"


def check(candidate):
    assert candidate(0) == "db0db"
    assert candidate(32) == "db100000db"
    assert candidate(103) == "db1100111db"
    assert candidate(15) == "db1111db"
    assert candidate(61239) == "db1110111100110111db"


def test_check():
    check(decimal_to_binary)