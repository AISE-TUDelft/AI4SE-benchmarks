def is_simple_power(x: int, n: int) -> bool:
    """
    Check if number x is a simple power of n.
    x is a simple power of n if n to the power of some integer equals x.
    For example:
        is_simple_power(1, 4) => true (4^0 = 1)
        is_simple_power(2, 2) => true (2^1 = 2)
        is_simple_power(8, 2) => true (2^3 = 8)
        is_simple_power(3, 2) => false (only 2 and 4 are neighbouring simple powers)
        is_simple_power(3, 1) => false (1 is not a simple power of any number besides itself)
    """
    if (n == 1):
        return (x == 1)
    power = 1
    while (abs(power) < abs(x)):
        power = power * n
    return (power == x)


def check(candidate):
    assert candidate(16, 2) == True
    assert candidate(143214, 16) == False
    assert candidate(4, 2) == True
    assert candidate(9, 3) == True
    assert candidate(16, 4) == True
    assert candidate(24, 2) == False
    assert candidate(128, 4) == False
    assert candidate(12, 6) == False
    assert candidate(1, 1) == True
    assert candidate(0, 1) == False
    assert candidate(1, 12) == True
    assert candidate(16, -2) == True
    assert candidate(-8, -2) == True
    assert candidate(-118587876497, -17) == True


def test_check():
    check(is_simple_power)