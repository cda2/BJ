from unittest import TestCase

from python.src.bj1074 import solution


class T1074(TestCase):
    def test1(self):
        self.assertEqual(solution(2, 3, 1), 11)

    def test2(self):
        self.assertEqual(solution(3, 7, 7), 63)

    def test3(self):
        self.assertEqual(solution(3, 1, 5), 19)

    def test4(self):
        self.assertEqual(solution(5, 2, 26), 332)
