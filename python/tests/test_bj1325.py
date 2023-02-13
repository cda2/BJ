from unittest import TestCase

from python.src.bj1325 import solution


class T1325(TestCase):
    def test1(self):
        self.assertEqual(solution(5, [[3, 1], [3, 2], [4, 3], [5, 3]]), [1, 2])

    def test2(self):
        self.assertEqual(solution(3, [[3, 2], [2, 1], [1, 3]]), [1, 2, 3])

    def test3(self):
        self.assertEqual(solution(5, [[3, 2], [4, 3], [3, 4], [4, 5]]), [2, 5])

    def test4(self):
        self.assertEqual(
            solution(
                12,
                [
                    [2, 1],
                    [3, 2],
                    [4, 2],
                    [5, 1],
                    [2, 5],
                    [6, 7],
                    [7, 8],
                    [8, 9],
                    [9, 10],
                    [10, 11],
                    [11, 12],
                ],
            ),
            [12],
        )


if __name__ == "__main__":
    import unittest
    unittest.main()
