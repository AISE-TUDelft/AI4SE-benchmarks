def fib(n: int) -> int:
    """
    Return the n-th Fibonacci number.
    
    Examples:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    assert n >= 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def check(candidate):
    assert candidate(0) == 0
    assert candidate(10) == 55
    assert candidate(1) == 1
    assert candidate(2) == 1
    assert candidate(3) == 2
    assert candidate(8) == 21
    assert candidate(11) == 89
    assert candidate(12) == 144
    assert candidate(39) == 63245986


def test_check():
    check(fib)