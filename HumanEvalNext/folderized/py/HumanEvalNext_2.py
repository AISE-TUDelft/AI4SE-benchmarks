def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    assert number > 0
    return number % 1.0


def check(candidate):
    assert candidate(3.5) == 0.5
    assert candidate(1.33) < 0.330001
    assert candidate(1.33) > 0.329999
    assert candidate(123.456) < 0.456001
    assert candidate(123.456) > 0.455999
    assert candidate(9.99999) < 0.99999001
    assert candidate(9.99999) > 0.99998999
    assert candidate(10.00001) < 0.00001001
    assert candidate(10.00001) > 0.00000999
    assert candidate(1.0) < 1e-6
    assert candidate(1.0) < 1.0
    assert candidate(1.13) < 1.0
    assert candidate(1.26) < 0.260001
    assert candidate(1.26) > 0.259999
    assert candidate(1.39) < 0.390001
    assert candidate(1.39) > 0.389999
    assert candidate(1.52) < 0.520001
    assert candidate(1.52) > 0.519999
    assert candidate(1.65) < 0.650001
    assert candidate(1.65) > 0.649999
    assert candidate(1.65) < 1.0
    assert candidate(1.78) < 1.0
    assert candidate(1.91) < 0.910001
    assert candidate(1.91) > 0.909999
    assert candidate(1.91) < 1.0
    assert candidate(2.04) < 1.0
    assert candidate(2.17) < 0.170001
    assert candidate(2.17) > 0.169999
    assert candidate(2.17) < 1.0
    assert candidate(2.3) < 1.0
    assert candidate(2.43) < 0.430001
    assert candidate(2.43) > 0.429999
    assert candidate(2.43) < 1.0


def test_check():
    check(truncate_number)