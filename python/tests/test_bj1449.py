from unittest import TestCase

from python.src.bj1449 import solution


class T1449(TestCase):
    def test1(self):
        self.assertEqual(solution(1, [1, 2, 3, 4, 5]), 5)

    def test2(self):
        self.assertEqual(solution(3, [1, 2, 3, 4]), 2)

    def test3(self):
        self.assertEqual(solution(2, [1, 2, 3, 4, 5]), 3)

    def test4(self):
        self.assertEqual(solution(3, [1, 2, 3, 4, 1000]), 3)

    def test5(self):
        self.assertEqual(solution(1000, [1, 1000]), 1)
