from unittest import TestCase

from python.src.bj2839 import solution


class T2839(TestCase):
    def test1(self):
        assert solution(18) == 4

    def test2(self):
        assert solution(4) == -1

    def test3(self):
        assert solution(6) == 2

    def test4(self):
        assert solution(9) == 3

    def test5(self):
        assert solution(11) == 3

    def test6(self):
        assert solution(27) == 7
