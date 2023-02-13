from unittest import TestCase

from python.src.bj1967 import solution


class T1967(TestCase):
    def test_solution1(self):
        assert solution(5, [[1, 3, 2], [3, 4, 3], [4, 2, 4], [4, 5, 6]]) == 11

    def test_solution2(self):
        assert solution(3, [[1, 2, 3], [1, 3, 50]]) == 53

    def test_solution3(self):
        assert solution(5, [[1, 5, 5], [5, 2, 2], [5, 3, 3], [5, 4, 4]]) == 9

    def test_solution4(self):
        assert solution(14,
                        [[1, 3, 90], [1, 5, 80], [1, 6, 70], [1, 13, 60],
                         [2, 4, 20],
                         [2, 7, 18], [3, 12, 100], [6, 10, 9], [6, 14, 11],
                         [13, 2, 3],
                         [13, 8, 2], [13, 9, 1], [13, 11, 4], ], ) == 273

    def test_solution5(self):
        assert solution(7,
                        [[1, 5, 100], [3, 7, 3], [5, 6, 50], [6, 2, 5],
                         [6, 3, 3],
                         [6, 4, 4]]) == 156
