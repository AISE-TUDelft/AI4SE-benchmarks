from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of one decimal place GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    
    For input out of bounds, return an empty string.
    Also, the grade needs to be rounded (half up) to 1 decimal place if needed,
    before being converted to a letter grade. For edge scenarios, consider a tolerance of 1e-6.

    Example:
        grade_equation([4.0, 3, 1.72, 2, 3.5, 4.5]) ==> ['A+', 'B', 'C-', 'C', 'A-', '']
    """
    tol = 1e-6
    
    import decimal
    def round_grade_with_tolerance(grade: decimal.Decimal, tol: float = tol) -> decimal.Decimal:
        rounded = grade.quantize(decimal.Decimal('1.0'), rounding=decimal.ROUND_HALF_UP)
        return rounded - decimal.Decimal(tol)

    letter_grade = []
    for gpa in [decimal.Decimal(str(grade)) for grade in grades]:
        if gpa > decimal.Decimal(4.0):
            letter_grade.append("")
        elif round_grade_with_tolerance(gpa, tol = 0.0) == decimal.Decimal(4.0):
            letter_grade.append("A+")
        elif round_grade_with_tolerance(gpa) > decimal.Decimal(3.7):
            letter_grade.append("A")
        elif round_grade_with_tolerance(gpa) > decimal.Decimal(3.3):
            letter_grade.append("A-")
        elif round_grade_with_tolerance(gpa) > decimal.Decimal(3.0):
            letter_grade.append("B+")
        elif round_grade_with_tolerance(gpa) > decimal.Decimal(2.7):
            letter_grade.append("B")
        elif round_grade_with_tolerance(gpa) > decimal.Decimal(2.3):
            letter_grade.append("B-")
        elif round_grade_with_tolerance(gpa) > decimal.Decimal(2.0):
            letter_grade.append("C+")
        elif round_grade_with_tolerance(gpa) > decimal.Decimal(1.7):
            letter_grade.append("C")
        elif round_grade_with_tolerance(gpa) > decimal.Decimal(1.3):
            letter_grade.append("C-")
        elif round_grade_with_tolerance(gpa) > decimal.Decimal(1.0):
            letter_grade.append("D+")
        elif round_grade_with_tolerance(gpa) > decimal.Decimal(0.7):
            letter_grade.append("D")
        elif gpa < decimal.Decimal(0.0):
            letter_grade.append("")
        elif round_grade_with_tolerance(gpa) > decimal.Decimal(0.0):
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade


def check(candidate):
    assert candidate([]) == []
    assert candidate([-1.5, 8.0, 10.0, 5.5]) == ['', '', '', '']
    assert candidate([4.0, 3, 1.72, 2, 3.5, 4.5]) == ['A+', 'B', 'C-', 'C', 'A-', '']
    assert candidate([1, 0.3, 1.5, 2.8, 3.3]) == ['D', 'D-', 'C-', 'B', 'B+']
    assert candidate([4.01, 4.001]) == ['', '']
    assert candidate([4.0, 3.95]) == ['A+', 'A+']
    assert candidate([3.75, 3.8, 3.94]) == ['A', 'A', 'A']
    assert candidate([3.35, 3.5, 3.6, 3.7, 3.74]) == ['A-', 'A-', 'A-', 'A-', 'A-']
    assert candidate([3.05, 3.1, 3.2, 3.3, 3.34]) == ['B+', 'B+', 'B+', 'B+', 'B+']
    assert candidate([2.75, 2.8, 2.9, 3.0, 3.04]) == ['B', 'B', 'B', 'B', 'B']
    assert candidate([2.35, 2.4, 2.5, 2.6, 2.74]) == ['B-', 'B-', 'B-', 'B-', 'B-']
    assert candidate([2.05, 2.1, 2.2, 2.3, 2.34]) == ['C+', 'C+', 'C+', 'C+', 'C+']
    assert candidate([1.75, 1.8, 1.9, 2.0, 2.04]) == ['C', 'C', 'C', 'C', 'C']
    assert candidate([1.35, 1.4, 1.5, 1.6, 1.74]) == ['C-', 'C-', 'C-', 'C-', 'C-']
    assert candidate([1.05, 1.1, 1.2, 1.3, 1.34]) == ['D+', 'D+', 'D+', 'D+', 'D+']
    assert candidate([0.75, 0.8, 0.9, 1.0, 1.04]) == ['D', 'D', 'D', 'D', 'D']
    assert candidate([0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.74]) == ['D-', 'D-', 'D-', 'D-', 'D-', 'D-', 'D-', 'D-']
    assert candidate([0.0, 0.04]) == ['E', 'E']
    assert candidate([-0.1, -0.01, -1, -10]) == ['', '', '', '']


def test_check():
    check(numerical_letter_grade)