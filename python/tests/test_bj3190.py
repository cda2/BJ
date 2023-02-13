from collections import deque
from unittest import TestCase

from ..src.bj3190 import Pos, Rot, solution


class T3190(TestCase):
    def test1(self):
        self.assertEqual(
            solution(
                size=6,
                apples={Pos(2, 3), Pos(1, 4), Pos(4, 2)},
                drs=deque([Rot(3, "D"), Rot(15, "L"), Rot(17, "D")]),
            ),
            9,
        )

    def test2(self):
        self.assertEqual(
            solution(
                size=10,
                apples={Pos(0, 1), Pos(0, 2), Pos(0, 3), Pos(0, 4)},
                drs=deque(
                    [
                        Rot(8, "D"),
                        Rot(10, "D"),
                        Rot(11, "D"),
                        Rot(13, "L"),
                    ]
                ),
            ),
            21,
        )

    def test3(self):
        self.assertEqual(
            solution(
                size=5,
                apples=set(),
                drs=deque(
                    [
                        Rot(4, "D"),
                        Rot(8, "D"),
                        Rot(12, "D"),
                        Rot(15, "D"),
                        Rot(20, "L"),
                    ]
                ),
            ),
            20,
        )

    def test4(self):
        self.assertEqual(
            solution(
                size=8,
                apples={Pos(4, 3), Pos(4, 7), Pos(1, 4)},
                drs=deque(
                    [
                        Rot(7, "D"),
                        Rot(11, "D"),
                        Rot(15, "D"),
                        Rot(18, "D"),
                        Rot(19, "D"),
                        Rot(20, "D"),
                    ]
                ),
            ),
            21,
        )
