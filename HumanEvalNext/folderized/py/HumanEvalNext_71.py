def triangle_area(a: int, b: int, c: int) -> float:
    """
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.

    Examples:
        triangle_area(3, 4, 5) == 6.00
        triangle_area(1, 2, 10) == -1
    """
    if a < 0 or b < 0 or c < 0:
        return -1

    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    s = (a + b + c)/2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area


def check(candidate):
    assert candidate(3, 4, 5) == 6.00
    assert candidate(1, 2, 10) == -1
    assert candidate(4, 8, 5) == 8.18
    assert candidate(2, 2, 2) == 1.73
    assert candidate(1, 2, 3) == -1
    assert candidate(10, 5, 7) == 16.25
    assert candidate(2, 6, 3) == -1
    assert candidate(1, 1, 1) == 0.43
    assert candidate(2, 2, 10) == -1


def test_check():
    check(triangle_area)