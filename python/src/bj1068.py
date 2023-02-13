from collections import deque
from sys import stdin


def solution(arr: list[int], del_node: int):
    sets: list[set] = [set() for i in range(len(arr))]
    root: int = -1
    q: deque = deque()
    count: int = 0
    for i, v in enumerate(arr):
        if v == del_node or i == del_node:
            continue
        elif v != -1:
            sets[v].add(i)
        else:
            root = i

    if root != -1 and root != del_node:
        q.append(root)

    while len(q) > 0:
        pop: int = q.popleft()
        if len(sets[pop]) == 0:
            count += 1
            continue
        for child in sets[pop]:
            q.append(child)

    return count


def solve():
    n: int = int(stdin.readline())
    array: list[int] = list(map(int, stdin.readline().strip().split()))
    del_node: int = int(stdin.readline())
    print(solution(array, del_node))


if __name__ == "__main__":
    solve()

# from problems.BJ1068 import solution
# from unittest import TestCase
#
#
# class T1068(TestCase):
#     def test1(self):
#         self.assertEqual(solution([-1, 0, 0, 1, 1], 2), 2)
#
#     def test2(self):
#         self.assertEqual(solution([-1, 0, 0, 1, 1], 1), 1)
#
#     def test3(self):
#         self.assertEqual(solution([-1, 0, 0, 1, 1], 0), 0)
#
#     def test4(self):
#         self.assertEqual(solution([-1, 0, 0, 2, 2, 4, 4, 6, 6], 4), 2)
#
#     def test5(self):
#         self.assertEqual(solution([-1, 0, 0], 0), 0)
#
#     def test6(self):
#         self.assertEqual(solution([-1, 0, 1], 2), 1)
#
#     def test7(self):
#         self.assertEqual(solution([-1, 0, 1, 2], 2), 1)
#
#     def test8(self):
#         self.assertEqual(solution([1, 4, 3, -1, 3, 1, 2, 0, 6, 6, 6, 1], 2), 3)
