def add(x: int, y: int) -> int:
    """
    Add the two numbers x and y.

    Examples:
        >>> add(2, 3)
        5
        >>> add(5, 7)
        12
    """
    return x + y


def check(candidate):
    assert candidate(0, 1) == 1
    assert candidate(1, 0) == 1
    assert candidate(2, 3) == 5
    assert candidate(5, 7) == 12
    assert candidate(7, 5) == 12
    assert candidate(-1, 1) == 0
    assert candidate(1, -1) == 0
    assert candidate(-1, -1) == -2
    assert candidate(0, 0) == 0
    assert candidate(-2, -3) == -5
    assert candidate(-8, 0) == -8
    assert candidate(993, -546) == 447
    assert candidate(-4, 0) == -4
    assert candidate(0, -7) == -7
    assert candidate(-232, -357) == -589
    assert candidate(290, -617) == -327
    assert candidate(-739, 348) == -391
    assert candidate(-54, -16) == -70
    assert candidate(483, -438) == 45
    assert candidate(-564, -116) == -680
    assert candidate(466, 689) == 1155
    assert candidate(675, -127) == 548
    assert candidate(-239, 943) == 704
    assert candidate(664, -40) == 624
    assert candidate(720, -26) == 694
    assert candidate(226, -545) == -319
    assert candidate(-395, 978) == 583
    assert candidate(-821, 986) == 165
    assert candidate(-552, 400) == -152
    assert candidate(248, 171) == 419
    assert candidate(70, -667) == -597
    assert candidate(409, -121) == 288
    assert candidate(-430, 686) == 256
    assert candidate(222, -664) == -442
    assert candidate(934, 960) == 1894
    assert candidate(-521, -80) == -601
    assert candidate(232, 862) == 1094
    assert candidate(-100, 125) == 25
    assert candidate(-112, -40) == -152
    assert candidate(190, -470) == -280
    assert candidate(-742, 458) == -284
    assert candidate(54, 289) == 343
    assert candidate(-270, 254) == -16
    assert candidate(262, 627) == 889
    assert candidate(-657, 30) == -627
    assert candidate(-606, -588) == -1194
    assert candidate(-640, 900) == 260
    assert candidate(304, -864) == -560
    assert candidate(195, -232) == -37
    assert candidate(969, 268) == 1237
    assert candidate(360, -59) == 301
    assert candidate(-592, -967) == -1559
    assert candidate(-137, -747) == -884
    assert candidate(444, -777) == -333
    assert candidate(244, -721) == -477
    assert candidate(-456, -446) == -902
    assert candidate(-465, -217) == -682
    assert candidate(581, 82) == 663
    assert candidate(-879, -461) == -1340
    assert candidate(158, 981) == 1139
    assert candidate(8, 558) == 566
    assert candidate(-242, -510) == -752
    assert candidate(36, -636) == -600
    assert candidate(-381, -563) == -944
    assert candidate(910, -888) == 22
    assert candidate(-849, -574) == -1423
    assert candidate(556, -163) == 393
    assert candidate(-872, 743) == -129
    assert candidate(321, 778) == 1099
    assert candidate(-651, -588) == -1239
    assert candidate(-303, -848) == -1151
    assert candidate(-833, 858) == 25
    assert candidate(312, 406) == 718
    assert candidate(-479, -823) == -1302
    assert candidate(-624, 581) == -43
    assert candidate(-995, 715) == -280
    assert candidate(-810, 931) == 121
    assert candidate(-193, -547) == -740
    assert candidate(221, -880) == -659
    assert candidate(798, 745) == 1543
    assert candidate(-62, -489) == -551
    assert candidate(21, -310) == -289
    assert candidate(281, 662) == 943
    assert candidate(652, -1000) == -348
    assert candidate(-790, 47) == -743
    assert candidate(148, -259) == -111
    assert candidate(-734, 163) == -571
    assert candidate(-779, 577) == -202
    assert candidate(-91, -688) == -779
    assert candidate(615, 193) == 808
    assert candidate(472, 685) == 1157
    assert candidate(-966, 210) == -756
    assert candidate(567, -990) == -423
    assert candidate(55, 401) == 456
    assert candidate(485, -827) == -342
    assert candidate(-208, 790) == 582
    assert candidate(-314, -417) == -731
    assert candidate(467, -247) == 220
    assert candidate(892, 780) == 1672
    assert candidate(532, 286) == 818
    assert candidate(602, 944) == 1546
    assert candidate(897, 888) == 1785
    assert candidate(76, 844) == 920
    assert candidate(-56, -208) == -264
    assert candidate(630, 521) == 1151
    assert candidate(-211, -535) == -746
    assert candidate(-398, -356) == -754
    assert candidate(811, -540) == 271
    assert candidate(83, 497) == 580
    assert candidate(-312, 169) == -143
    assert candidate(632, -176) == 456
    assert candidate(-808, -709) == -1517
    assert candidate(-16, 636) == 620


def test_check():
    check(add)