from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string possibly containing multiple groups of nested parentheses.
    Your goal is to separate those groups into separate strings and return the list of those.
    Ignore anything other than "(" and ")" in the input string.

    Examples:
        >>> seperate_paren_groups('(()())')
        ['(()())']
        >>> separate_paren_groups('()(())')
        ['()', '(())']
        >>> separate_paren_groups(')( [) (( ))] (({})( ))')
        ['()', '(())', '(()())']
    """
    input = "".join([x for x in paren_string if x in '()'])
    breakpoints = input.split('()')
    groups = []

    for i in range(len(breakpoints) - 1):
        group = '()'
        while breakpoints[i] != "" and breakpoints[i].endswith('(') and breakpoints[i + 1] != "" and breakpoints[i + 1].startswith(')'):
            group = f"({group})"
            breakpoints[i] = breakpoints[i][:-1]
            breakpoints[i + 1] = breakpoints[i + 1][1:]
        groups.append(group)

    while '' in breakpoints:
        start = None
        middle = False
        end = None

        for i in range(len(breakpoints)):
            if breakpoints[i].endswith('('):
                start = i
                middle = False
                end = None
            elif breakpoints[i] == "" and start is not None:
                middle = True
            elif breakpoints[i].startswith(')') and middle:
                end = i
                break

        if start is not None and end is not None:
            chained = "".join(groups[start:end])
            while breakpoints[start] != "" and breakpoints[start].endswith('(') and breakpoints[end] != "" and breakpoints[end].startswith(')'):
                chained = f"({chained})"
                breakpoints[start] = breakpoints[start][:-1]
                breakpoints[end] = breakpoints[end][1:]

            groups = groups[:start] + [chained] + groups[end:]
            breakpoints = breakpoints[:start] + [breakpoints[start]] + breakpoints[end:]
        else:
            break

    return groups


def check(candidate):
    assert candidate('()') == ['()']
    assert candidate('()()') == ['()', '()']
    assert candidate('(())') == ['(())']
    assert candidate('') == []
    assert candidate('True') == []
    assert candidate('{}') == []
    assert candidate('((') == []
    assert candidate('))') == []
    assert candidate('((())') == ['(())']
    assert candidate('(()))') == ['(())']
    assert candidate('((())(()))') == ['((())(()))']
    assert candidate('(()(())((())))') == ['(()(())((())))']
    assert candidate('))))))))))))))))))(((((((((((((((((((((((((((((((())(((((((((((((((((((') == ['(())']
    assert candidate('()))()(())(()))') == ['()', '()', '(())', '(())']
    assert candidate('))())))((((())(((((((())))((') == ['()', '(())', '(((())))']
    assert candidate(')(  )(  )(') == ['()', '()']
    assert candidate('(([()]))') == ['((()))']
    assert candidate('(()---())') == ['(()())']
    assert candidate('(     )() () ') == ['()', '()', '()']
    assert candidate('((o)()) (((0))) () (((O))(@)(.))') == ['(()())', '((()))', '()', '((())()())']
    assert candidate('((()((()(()))))) ((([])([])([])([])([])))') == ['((()((()(())))))', '((()()()()()))']
    assert candidate('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    assert candidate('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert candidate('  (    ) ( ( )) (( )     ( ))  ') == ['()', '(())', '(()())']
    assert candidate('\(O_O)/ \(o_o)/ \(O_o)/ \(o_O)/') == ['()', '()', '()', '()']


def test_check():
    check(separate_paren_groups)