from unittest import TestCase

from python.src.bj1520 import solution


class T1520(TestCase):
    def test1(self):
        self.assertEqual(
            solution(
                (4, 5),
                [
                    [50, 45, 37, 32, 30],
                    [35, 30, 40, 20, 25],
                    [30, 30, 25, 17, 28],
                    [27, 24, 22, 15, 10],
                ],
            ),
            3,
        )

    def test2(self):
        self.assertEqual(solution((3, 3), [[5, 4, 3], [4, 3, 2], [3, 2, 6]]), 0)
