from unittest import TestCase

from python.src.bj2468 import solution


class T2468(TestCase):
    def test1(self):
        self.assertEqual(
            solution(
                5,
                [
                    [6, 8, 2, 6, 2],
                    [3, 2, 3, 4, 6],
                    [6, 7, 3, 3, 2],
                    [7, 2, 5, 3, 6],
                    [8, 9, 5, 2, 7],
                ],
            ),
            5,
        )

    def test2(self):
        self.assertEqual(
            solution(
                5,
                [
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                ],
            ),
            1,
        )

    def test3(self):
        self.assertEqual(solution(2, [[1, 1], [1, 1]]), 1)
