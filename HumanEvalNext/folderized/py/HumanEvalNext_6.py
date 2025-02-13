from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string containing "(" and ")"s (not exclusively),
    possibly including multiple groups for nested parentheses.
    For each of these groups, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three and )( has zero.

    Example:
        >>> parse_nested_parens('{\"example\": \"(()[]()) ((()))()((())()() )\"}')
        [2, 3, 1, 3]
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
            breakpoints = breakpoints[:start] + \
                [breakpoints[start]] + breakpoints[end:]
        else:
            break
    
    def depth(s):
        max_depth = 0
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif c == ')':
                depth -= 1
        return max_depth

    return [depth(group) for group in groups]


def check(candidate):
    assert candidate('') == []
    assert candidate('(())') == [2]
    assert candidate(')(') == []
    assert candidate('((') == []
    assert candidate('))') == []
    assert candidate('((())') == [2]
    assert candidate('(()))') == [2]
    assert candidate('()') == [1]
    assert candidate('((()))') == [3]
    assert candidate('(()())') == [2]
    assert candidate('()()') == [1, 1]
    assert candidate(' )(  )(  )( ') == [1, 1]
    assert candidate('))))))))))))))))))(((((((((((((((((((((((((((((((())(((((((((((((((((((') == [2]
    assert candidate('True') == []
    assert candidate('(     )()\t () ') == [1, 1, 1]
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() ((\n)) ((())) ((((-))))') == [1, 2, 3, 4]
    assert candidate('((o)((O))(((0))))))))))') == [4]
    assert candidate('((  ) (()  )   (( ())))   ') == [4]
    assert candidate('((()((()(()))))) ((([])([])([])([])([])))') == [6, 3]
    assert candidate('((a)(b)) (((!)))(c) (   {} (())(___)() ))') == [2, 3, 1, 3]
    assert candidate('{\"example\": \"(()[]()) ((()))()((())()() )\"}') == [2, 3, 1, 3]


def test_check():
    check(parse_nested_parens)