from sys import stdin


def solution(n: int, r: int, c: int) -> int:
    result: int = 0
    while n > 0:
        small_sqr_len: int = 2 ** (n - 1)
        rb, cb = quadrant(small_sqr_len, r, c)
        if rb:
            r -= small_sqr_len
            result += small_sqr_len * small_sqr_len * 2
        if cb:
            c -= small_sqr_len
            result += small_sqr_len * small_sqr_len
        n -= 1
    return result


def quadrant(q: int, r: int, c: int) -> tuple[bool, bool]:
    return r >= q, c >= q


def solve():
    n, r, c = map(int, stdin.readline().strip().split())
    print(solution(n=n, r=r, c=c))


if __name__ == "__main__":
    solve()

# from unittest import TestCase
#
# from problems.BJ1074 import solution
#
#
# class T1074(TestCase):
#     def test1(self):
#         self.assertEqual(solution(2, 3, 1), 11)
#
#     def test2(self):
#         self.assertEqual(solution(3, 7, 7), 63)
