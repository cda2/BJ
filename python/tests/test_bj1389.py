from unittest import TestCase

from python.src.bj1389 import solution


class T1389(TestCase):
    def test1(self):
        self.assertEqual(solution(5, [[1, 3], [1, 4], [4, 5], [4, 3], [3, 2]]), 3)
