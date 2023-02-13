from unittest import TestCase

from python.src.bj7576 import solution


class T7576(TestCase):
    def test1(self):
        assert solution(
            6,
            4,
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
            ],
        ) == 8

    def test2(self):
        assert solution(
            6,
            4,
            [
                [0, -1, 0, 0, 0, 0],
                [-1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
            ],
        ) == -1

    def test3(self):
        assert solution(
            6,
            4,
            [
                [1, -1, 0, 0, 0, 0],
                [0, -1, 0, 0, 0, 0],
                [0, 0, 0, 0, -1, 0],
                [0, 0, 0, 0, -1, 1],
            ],
        ) == 6

    def test4(self):
        assert solution(
            5,
            5,
            [
                [
                    -1,
                    1,
                    0,
                    0,
                    0,
                ],
                [0, -1, -1, -1, 0],
                [0, -1, -1, -1, 0],
                [0, -1, -1, -1, 0],
                [0, 0, 0, 0, 0],
            ],
        ) == 14

    def test5(self):
        assert solution(2, 2, [[1, -1], [-1, 1]]) == 0

    def test6(self):
        assert solution(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 0]]) == 1

    def test7(self):
        assert solution(2, 2, [[1, 1], [1, 1]]) == 0
