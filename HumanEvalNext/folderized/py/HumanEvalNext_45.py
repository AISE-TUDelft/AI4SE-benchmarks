def triangle_area(a: float, h: float) -> float:
    """
    Given length of a side and height, return area for a triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return abs(a) * abs(h) / 2.0


def check(candidate):
    assert candidate(3, 5) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0
    assert candidate(0, 0) == 0.0
    assert candidate(2, -8) == 8.0
    assert candidate(-8, 2) == 8.0


def test_check():
    check(triangle_area)