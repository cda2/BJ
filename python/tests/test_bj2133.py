from unittest import TestCase

from python.src.bj2133 import solution


class T2133(TestCase):
    def test_solution1(self):
        assert solution(4) == 11

    def test_solution2(self):
        assert solution(6) == 41

    def test_solution3(self):
        assert solution(8) == 153

    def test_solution4(self):
        assert solution(12) == 2131
