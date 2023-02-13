from collections import defaultdict
from sys import setrecursionlimit, stdin
from typing import *


def solution(map_size: Tuple[int, int], map_data: list) -> int:
    # return bfs(map_size, map_data)
    visited: defaultdict = defaultdict(bool)
    return dfs((0, 0), visited=visited, map_size=map_size, map_data=map_data)


# def bfs(map_size: Tuple[int, int], map_data: List) -> int:
#     q: deque = deque()
#     result: int = 0
#     q.append(((0, 0), (0, 0)))
#     while len(q) > 0:
#         cur_pos, prev_pos = q.popleft()
#         if cur_pos == (map_size[0] - 1, map_size[1] - 1):
#             result += 1
#         for next_p in next_pos(pos=cur_pos, map_size=map_size):
#             if next_p != prev_pos and map_data[cur_pos[0]][cur_pos[1]] > map_data[next_p[0]][next_p[1]]:
#                 q.append((next_p, cur_pos))
#     return result


def dfs(
    pos: Tuple[int, int],
    visited: defaultdict,
    map_size: Tuple[int, int],
    map_data: list,
) -> int:
    if pos == (map_size[0] - 1, map_size[1] - 1):
        return 1
    result: int = 0
    for np in next_pos(pos=pos, map_size=map_size):
        if not visited[np] and compare(cur_pos=pos, after_pos=np,
                                       map_data=map_data):
            visited[np] = True
            result += dfs(pos=np, visited=visited, map_size=map_size,
                          map_data=map_data)
            visited[np] = False
    return result


def next_pos(pos: Tuple[int, int], map_size: Tuple[int, int]) -> List[
    Tuple[int, int]]:
    result: list = []
    if pos[0] < map_size[0] - 1:
        result.append((pos[0] + 1, pos[1]))
    if 0 < pos[1]:
        result.append((pos[0], pos[1] - 1))
    if pos[1] < map_size[1] - 1:
        result.append((pos[0], pos[1] + 1))
    return result


def compare(
    cur_pos: Tuple[int, int], after_pos: Tuple[int, int], map_data: list
) -> bool:
    if map_data[cur_pos[0]][cur_pos[1]] > map_data[after_pos[0]][after_pos[1]]:
        return True
    return False


def solve():
    setrecursionlimit(10 ** 9)
    m, n = map(int, stdin.readline().strip().split())
    world_map: list = [
        list(map(int, stdin.readline().strip().split())) for _ in range(m)
    ]
    print(solution((m, n), world_map))


if __name__ == "__main__":
    solve()
