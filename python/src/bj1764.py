from collections.abc import Iterable
from sys import stdin


def solution(not_heard: Iterable, not_seen: Iterable):
    not_heard: set = set(not_heard)
    not_seen: set = set(not_seen)
    intersection: list[str] = list(not_heard.intersection(not_seen))
    intersection.sort()
    return intersection


def solve():
    n, m = map(int, stdin.readline().split())
    not_heard: list[str] = [stdin.readline().strip() for i in range(n)]
    not_seen: list[str] = [stdin.readline().strip() for i in range(m)]
    result: list = solution(not_heard, not_seen)
    print(len(result))
    for i in result:
        print(i)


if __name__ == "__main__":
    solve()
