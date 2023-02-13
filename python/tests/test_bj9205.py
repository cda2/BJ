import unittest

from python.src.bj9205 import solution


class T1325(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solution((0, 0), (2000, 1000), [(1000, 0), (1000, 1000)]), "happy"
        )

    def test2(self):
        self.assertEqual(
            solution((0, 0), (2000, 2000), [(1000, 0), (2000, 1000)]), "sad"
        )

    def test3(self):
        self.assertEqual(solution((1000, 1000), (1000, 1001), []), "happy")

    def test4(self):
        self.assertEqual(solution((0, 0), (0, 2000), [(1000, 0)]), "sad")

    def test5(self):
        self.assertEqual(solution((0, 0), (0, 2000), [(10000, 0), (0, 1000)]), "happy")
