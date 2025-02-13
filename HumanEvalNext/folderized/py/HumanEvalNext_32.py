import math
from typing import List


def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: List[int]) -> float:
    """
    xs are coefficients of a polynomial.
    Find x such that poly(x) = 0 and return only one zero point, even if there are many.
    
    Constraints:
        List xs should have an even number of coefficients
        and as largest a non-zero coefficient to guarantee a solution.

    Examples:
        >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
        -0.5
        >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
        1.0
    """
    begin, end = -1., 1.
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin


def check(candidate):
    assert abs(candidate([-10, -2]) - (-5.000000000058208)) < 1e-6
    assert abs(candidate([-3, -6, -7, 7]) - (1.6679422343731858)) < 1e-6
    assert abs(candidate([8, 3]) - (-2.666666666686069)) < 1e-6
    assert abs(candidate([-10, -8]) - (-1.2500000000582077)) < 1e-6
    assert abs(candidate([-3, 6, 9, -10]) - (-0.6685768984025344)) < 1e-6
    assert abs(candidate([10, 7, 3, -3]) - (2.4815587521297857)) < 1e-6
    assert abs(candidate([8, -2, -10, -5, 3, 1, -2, -6]) - (0.7057115506613627)) < 1e-6
    assert abs(candidate([1, -7, -8, 2]) - (-0.8446386614232324)) < 1e-6
    assert abs(candidate([1, 1]) - (-1.0)) < 1e-6
    assert abs(candidate([-9, 4, 7, -7, 2, -8]) - (-0.8164280389901251)) < 1e-6
    assert abs(candidate([10, 9, 1, 8, -4, -8]) - (-0.8227368473890238)) < 1e-6
    assert abs(candidate([-3, -1]) - (-3.0000000000582077)) < 1e-6
    assert abs(candidate([-3, -7]) - (-0.42857142857974395)) < 1e-6
    assert abs(candidate([-2, 4, 10, 1, -5, 1, 1, -4]) - (-0.86899654957233)) < 1e-6
    assert abs(candidate([10, -8, 9, 10, -5, 7]) - (-1.0731038876692764)) < 1e-6
    assert abs(candidate([-5, 4, 2, -2]) - (-1.4836825707461685)) < 1e-6
    assert abs(candidate([1, -9, -3, -9]) - (0.10615823022089899)) < 1e-6
    assert abs(candidate([2, -2, -8, -4, 8, 1]) - (0.38501966872718185)) < 1e-6
    assert abs(candidate([10, 5, 2, 10]) - (-0.8933422100380994)) < 1e-6
    assert abs(candidate([-6, -2, -6, -3, 7, 7, -2, 8]) - (0.9600705468910746)) < 1e-6
    assert abs(candidate([8, 2, 1, -3, -6, 6, 5, -8]) - (1.1312649988103658)) < 1e-6
    assert abs(candidate([-7, -6]) - (-1.1666666666860692)) < 1e-6
    assert abs(candidate([3, 9, -8, 2]) - (-0.2661688190419227)) < 1e-6
    assert abs(candidate([9, 4, 6, -2, 7, -10, -7, 7]) - (-1.2858021691790782)) < 1e-6
    assert abs(candidate([10, 1, -7, -1, 3, -5]) - (1.0328693957999349)) < 1e-6
    assert abs(candidate([-10, -2, 6, -5, 6, -7, 10, -1]) - (-0.7015198637964204)) < 1e-6
    assert abs(candidate([-6, 1, -5, 7]) - (1.1949840254965238)) < 1e-6
    assert abs(candidate([9, 1]) - (-9.000000000058208)) < 1e-6
    assert abs(candidate([-10, -7, 1, -1, -3, -9, -3, 8]) - (1.5114667361485772)) < 1e-6
    assert abs(candidate([-8, 5]) - (1.599999999976717)) < 1e-6
    assert abs(candidate([7, -6]) - (1.1666666666278616)) < 1e-6
    assert abs(candidate([5, 7, -5, -2]) - (-0.547214484482538)) < 1e-6
    assert abs(candidate([-4, 7, -4, -1, 2, 10, 1, 4]) - (0.6221468804869801)) < 1e-6
    assert abs(candidate([-7, -3, -3, -8, 1, -10, 8, 7]) - (-0.7463565783691593)) < 1e-6
    assert abs(candidate([8, -3, -10, -8]) - (0.6355658151442185)) < 1e-6
    assert abs(candidate([-3, -8]) - (-0.37500000005820766)) < 1e-6
    assert abs(candidate([1, -8]) - (0.12499999994179234)) < 1e-6
    assert abs(candidate([-2, 5, -4, 7]) - (0.4360383356688544)) < 1e-6
    assert abs(candidate([8, 8, 5, -3]) - (2.9021427524276078)) < 1e-6
    assert abs(candidate([3, -4, -7, -7, 3, 1, 3, 3]) - (0.39456867933040485)) < 1e-6
    assert abs(candidate([-9, 10, 10, -7, -9, 2, 1, -7]) - (-1.0938426014618017)) < 1e-6
    assert abs(candidate([-4, -4, 7, 4]) - (-2.0)) < 1e-6
    assert abs(candidate([3, -5, -2, 4]) - (0.6513878188561648)) < 1e-6
    assert abs(candidate([-8, 4, 7, -7]) - (-0.9312933354522102)) < 1e-6
    assert abs(candidate([10, 7]) - (-1.428571428579744)) < 1e-6
    assert abs(candidate([-8, -3]) - (-2.666666666686069)) < 1e-6
    assert abs(candidate([3, 5, 5, -4]) - (2.0420076226000674)) < 1e-6
    assert abs(candidate([-9, -5, 2, -10, 2, -2, 4, -1]) - (-0.6912827867781743)) < 1e-6
    assert abs(candidate([7, 5, -6, -4, -1, -4, -9, 8]) - (-0.7303538502892479)) < 1e-6
    assert abs(candidate([1, -9]) - (0.11111111106583849)) < 1e-6
    assert abs(candidate([8, 5]) - (-1.6000000000349246)) < 1e-6
    assert abs(candidate([-9, 6, -8, -5]) - (-2.4085229280171916)) < 1e-6
    assert abs(candidate([9, -8]) - (1.1249999999417923)) < 1e-6
    assert abs(candidate([2, -7, 8, -3]) - (0.6666666666278616)) < 1e-6
    assert abs(candidate([9, -8]) - (1.1249999999417923)) < 1e-6
    assert abs(candidate([8, 8, 6, 1, -2, -4, 1, -3]) - (1.267006399051752)) < 1e-6
    assert abs(candidate([2, -6, 10, -1, 4, 1]) - (-4.72142661397811)) < 1e-6
    assert abs(candidate([-10, 4]) - (2.4999999999417923)) < 1e-6
    assert abs(candidate([-8, 7]) - (1.142857142840512)) < 1e-6
    assert abs(candidate([6, -2, -6, 1]) - (0.9066398076247424)) < 1e-6
    assert abs(candidate([-3, 1]) - (2.9999999999417923)) < 1e-6
    assert abs(candidate([-5, 4, 7, -1, 9, 10]) - (0.5266727519920096)) < 1e-6
    assert abs(candidate([7, -1]) - (6.999999999941792)) < 1e-6
    assert abs(candidate([-6, -2]) - (-3.0000000000582077)) < 1e-6
    assert abs(candidate([-7, 7]) - (0.9999999999417923)) < 1e-6
    assert abs(candidate([-2, -1, 9, -4]) - (-0.3903882032027468)) < 1e-6
    assert abs(candidate([-4, 10, -2, 6, 5, -2]) - (0.38592179998522624)) < 1e-6
    assert abs(candidate([-8, 10]) - (0.7999999999883585)) < 1e-6
    assert abs(candidate([-2, -9, -10, 1, -6, 10, -2, -5]) - (-1.9016489709028974)) < 1e-6
    assert abs(candidate([7, 3, 7, -10, -7, -8, -6, 7]) - (0.877888614195399)) < 1e-6
    assert abs(candidate([1, 8]) - (-0.12500000005820766)) < 1e-6
    assert abs(candidate([3, -6, -9, -1]) - (0.3303229847806506)) < 1e-6
    assert abs(candidate([-9, 1, -4, -3, -7, 1]) - (7.4735223380848765)) < 1e-6
    assert abs(candidate([9, -6, -3, -5, -5, 3, -10, -5]) - (0.6800906549324282)) < 1e-6
    assert abs(candidate([3, -3, -2, -5, -7, 2]) - (-1.0)) < 1e-6
    assert abs(candidate([5, -3]) - (1.6666666666278616)) < 1e-6
    assert abs(candidate([4, 1, -1, -3]) - (1.091414260212332)) < 1e-6
    assert abs(candidate([-10, -4, 2, 1]) - (2.1179422714048997)) < 1e-6
    assert abs(candidate([-8, -2, 1, 10, 6, 2]) - (0.8199922735802829)) < 1e-6
    assert abs(candidate([-10, -7, -2, -5, 8, -2]) - (-0.7751165542285889)) < 1e-6
    assert abs(candidate([-7, 9]) - (0.7777777777519077)) < 1e-6
    assert abs(candidate([1, 1, 3, 9, 6, -7, 2, 8]) - (-1.0796475561219268)) < 1e-6
    assert abs(candidate([-2, -9, 3, -10]) - (-0.20000000001164153)) < 1e-6
    assert abs(candidate([1, 3, -8, 1]) - (-0.2112208516919054)) < 1e-6
    assert abs(candidate([-7, -1, 6, -1, 3, 1]) - (0.9578598753432743)) < 1e-6
    assert abs(candidate([-1, 7, -6, -4, 3, 2, -5, 9]) - (0.17007400892907754)) < 1e-6
    assert abs(candidate([2, 7, -10, -1, -1, -4]) - (0.746446434292011)) < 1e-6
    assert abs(candidate([8, 9, 10, 1, 4, 4, 4, -4]) - (2.018535319773946)) < 1e-6
    assert abs(candidate([-5, -8, -1, 6, 10, 9, 1, -8]) - (-0.7318775289459154)) < 1e-6
    assert abs(candidate([-1, -3, -4, -6]) - (-0.42038060672348365)) < 1e-6
    assert abs(candidate([-9, -3]) - (-3.0000000000582077)) < 1e-6
    assert abs(candidate([9, -8, 4, 3, 10, 8, -4, 2]) - (-1.2079210819210857)) < 1e-6
    assert abs(candidate([2, -3, -6, 10, -10, -7, 3, -3]) - (0.4243725821143016)) < 1e-6
    assert abs(candidate([6, 4, -9, 7]) - (-0.5456791458418593)) < 1e-6
    assert abs(candidate([-7, 4, -6, 4]) - (1.5720202162628993)) < 1e-6
    assert abs(candidate([4, 9, 6, 3, 7, 4]) - (-1.4282608788926154)) < 1e-6
    assert abs(candidate([5, 4, -2, -3]) - (1.313795538211707)) < 1e-6
    assert abs(candidate([6, 5, 10, -3, -2, 4]) - (-1.3557373622315936)) < 1e-6
    assert abs(candidate([-1, -3]) - (-0.33333333337213844)) < 1e-6
    assert abs(candidate([1, 1, 7, -8, -6, -6]) - (0.696112065052148)) < 1e-6


def test_check():
    check(find_zero)