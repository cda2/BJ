from unittest import TestCase

from python.src.bj1744 import solution


class T1744(TestCase):
    def test_case_1(self):
        assert solution([-5, -2, -1, 0, 3, 6]) == 28

    def test_case_2(self):
        assert solution([3, 9, 4, 3, 3]) == 48

    def test_case_3(self):
        assert solution([1, 2]) == 3

    def test_case_4(self):
        assert solution([-10, -9, -8, -7, -6, -5, 1, 2, 3, 4, 5, 6, 7]) == 245

    def test_case_5(self):
        assert solution([-5, -4, -3, 0, 1, 2, 3, 4, 5, 6]) == 65

    def test_case_6(self):
        assert solution([-1, -2, 0, 0, 0]) == 2

    def test_case_7(self):
        assert solution([-5, -4, -3, -2, -1]) == 25

    def test_case_8(self):
        assert solution([1, 1, 1, 1, 1]) == 5

    def test_case_9(self):
        assert solution([-3, -2, -1, 1, 2]) == 8

    def test_case_10(self):
        assert solution([-6, -5, -1]) == 29

    def test_case_11(self):
        assert solution([-5, -4, -3, 0, 1, 2, 3, 4, 5, 6]) == 65

    def test_case_12(self):
        assert solution([-3, -2, -1, 1, 2]) == 8

    def test_case_13(self):
        assert solution([-1, 0, 1]) == 1
