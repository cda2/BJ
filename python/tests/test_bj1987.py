from unittest import TestCase

from python.src.bj1987 import solution


class T1987(TestCase):
    def test_solution1(self):
        assert solution(2, 4, [list("CAAB"), list("ADCB")]) == 3

    def test_solution2(self):
        assert solution(
            20,
            20,
            [
                list("YACDEFBXZJKVAXZXBSVA"),
                list("BCDEFGHIJKLMNSVUTBSV"),
                list("CDEFGHIJKLMNORTXUTBS"),
                list("DEFGHIJKLMNOPQWZXUTW"),
                list("AFGHIJKLMNOPQRSVZXWT"),
                list("XGHIJKLMNOPQRSTBXZVU"),
                list("WHIJKLMNOPQRSTUVWXZZ"),
                list("HIJKLMNOPQRSTUVZXWZA"),
                list("IJKLMNOPQRSTUVWXZZAB"),
                list("JKLMNOPQRSTUVZXWZABC"),
                list("TLMNOPQRSTUVWXWZABCD"),
                list("QZNOPQRSTUVZXZZABCDE"),
                list("ZRSPQRSTUVZXWZABCDEF"),
                list("AVUXTSTUVZXWZABCDEFG"),
                list("ZBWUAWXVWXWZABCDEFGH"),
                list("ZRVWVUWAXZZABCDEFGHI"),
                list("SRZVZVAXZZABCDEFGHIJ"),
                list("TSRZSBUZZABCDEFGHIJK"),
                list("QTSRTXZZABCDEFGHIJKL"),
                list("CQTQQZZABCDEFGHIJKLM"),
            ],
        ) == 26

    def test_solution3(self):
        assert solution(
            20,
            20,
            [
                list("YBCDEFGHUJZAQFOJRQXH"),
                list("HAXNLTWMSKIVAPNOJZQD"),
                list("PMCOSPIJQPREGQZPFLRU"),
                list("VDGIWVDFHUAHFKUJHAOX"),
                list("TQKLUZPLRQOQUVIDJOZI"),
                list("ZFRJRTTHUGTJNIXKGUBC"),
                list("UHPASLMQZAMRIKQJOEZA"),
                list("MTZHFKJGJKQJKZWOAZAA"),
                list("VUTGSVFQRITNFSBCEAAB"),
                list("MWDQFTAKDFMGIOCEAABC"),
                list("SQVFEQXRBAUPRMEAABCD"),
                list("FGWUVWKIAENSCEAABCDE"),
                list("KVSXEZXDENBHAAABCDEF"),
                list("SEEJSKPENBPAAABCDEFG"),
                list("NFUAWDUCHPFAABCDEFGH"),
                list("SMLFVTRMHGAABCDEFGHI"),
                list("HNINXFMFEAABCDEFGHIJ"),
                list("FMJQJOGEAABCDEFGHIJK"),
                list("QFOFOFEAABCDEFGHIJKL"),
                list("AHFOAAAABCDEFGHIJKLM"),
            ],
        ) == 26

    def test_solution4(self):
        assert solution(
            20,
            20,
            [
                list("AYXWVUTSRQPONMLKJIHG"),
                list("YXWVUTSRQPONMLKJIHGF"),
                list("XWVUTSRQPONMLKJIHGFE"),
                list("WVUTSRQPONMLKJIHGFED"),
                list("VUTSRQPONMLKJIHGFEDC"),
                list("UTSRQPONMLKJIHGFEDCB"),
                list("TSRQPONMLKJIHGFEDCBA"),
                list("SRQPONMLKJIHGFEDCBAA"),
                list("RQPONMLKJIHGFEDCBAAA"),
                list("QPONMLKJIHGFEDCBAAAA"),
                list("PONMLKJIHGFEDCBAAAAA"),
                list("ONMLKJIHGFEDCBAAAAAA"),
                list("NMLKJIHGFEDCBAAAAAAA"),
                list("MLKJIHGFEDCBAAAAAAAA"),
                list("LKJIHGFEDCBAAAAAAAAA"),
                list("KJIHGFEDCBAAAAAAAAAA"),
                list("JIHGFEDCBAAAAAAAAAAA"),
                list("IHGFEDCBAAAAAAAAAAAA"),
                list("HGFEDCBAAAAAAAAAAAAA"),
                list("GFEDCBAAAAAAAAAAAAAA"),
            ],
        ) == 25
