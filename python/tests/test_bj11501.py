from unittest import TestCase

from python.src.bj11501 import solution


class T11501(TestCase):
    def test1(self):
        self.assertEqual(39, solution([1, 2, 5, 4, 3, 7, 6, 5, 9, 8]))

    def test2(self):
        self.assertEqual(4, solution([2, 2, 1, 3]))

    def test3(self):
        self.assertEqual(10, solution([1, 2, 3, 4, 5]))

    def test_base1(self):
        self.assertEqual(0, solution([10, 7, 6]))

    def test_base2(self):
        self.assertEqual(10, solution([3, 5, 9]))

    def test_base3(self):
        self.assertEqual(5, solution([1, 1, 3, 1, 2]))
