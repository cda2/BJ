from collections import deque, namedtuple
from sys import stdin
from typing import Iterator

Pos: namedtuple = namedtuple("Pos", ["row", "col"])


def solution(size: int, data: list[list[int]]) -> int:
    result: int = -1
    max_height: int = max([max(data[i]) for i in range(size)])
    for h in range(0, max_height + 1):
        result = max(result, safe_group_count(size=size, map_dat=data, height=h))
    return result


def safe_group_count(size: int, map_dat: list[list[int]], height: int) -> int:
    flooded: list[list[bool]] = [[False for _ in range(size)] for _ in range(size)]
    count: int = 0
    for i in range(size):
        for j in range(size):
            if map_dat[i][j] <= height:
                flooded[i][j] = True
    for i in range(size):
        for j in range(size):
            if not flooded[i][j]:
                count += find_group(
                    size=size, flooded=flooded, start_pos=Pos(row=i, col=j)
                )
    return count


def find_group(size: int, flooded: list[list[bool]], start_pos: Pos) -> int:
    q: deque = deque()
    q.append(start_pos)

    while q:
        pop_pos: Pos = q.popleft()
        for np in available_near_pos(size=size, flooded=flooded, cur_pos=pop_pos):
            if flooded[np.row][np.col] is False:
                flooded[np.row][np.col] = True
                q.append(np)
    return 1


def available_near_pos(
    size: int, flooded: list[list[bool]], cur_pos: Pos
) -> Iterator[Pos]:
    for np in near_pos(cur_pos):
        if 0 <= np.row < size and 0 <= np.col < size:
            if not flooded[np.row][np.col]:
                yield np


def near_pos(pos: Pos) -> list[Pos]:
    return [
        Pos(pos.row - 1, pos.col),
        Pos(pos.row, pos.col + 1),
        Pos(pos.row + 1, pos.col),
        Pos(pos.row, pos.col - 1),
    ]


def solve():
    n: int = int(stdin.readline())
    map_data: list[list[int]] = [
        list(map(int, stdin.readline().strip().split())) for i in range(n)
    ]
    print(solution(size=n, data=map_data))


if __name__ == "__main__":
    solve()
