from unittest import TestCase

from python.src.bj1068 import solution


class T1068(TestCase):
    def test1(self):
        self.assertEqual(solution([-1, 0, 0, 1, 1], 2), 2)

    def test2(self):
        self.assertEqual(solution([-1, 0, 0, 1, 1], 1), 1)

    def test3(self):
        self.assertEqual(solution([-1, 0, 0, 1, 1], 0), 0)

    def test4(self):
        self.assertEqual(solution([-1, 0, 0, 2, 2, 4, 4, 6, 6], 4), 2)

    def test5(self):
        self.assertEqual(solution([-1, 0, 0], 0), 0)

    def test6(self):
        self.assertEqual(solution([-1, 0, 1], 2), 1)

    def test7(self):
        self.assertEqual(solution([-1, 0, 1, 2], 2), 1)

    def test8(self):
        self.assertEqual(solution([1, 4, 3, -1, 3, 1, 2, 0, 6, 6, 6, 1], 2), 3)
