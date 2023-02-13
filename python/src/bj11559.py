from collections import deque
from typing import Tuple


def solution(map_data: list):
    result: int = 0
    while True:
        bomb_set: set = set()
        for i in range(11, -1, -1):
            for j in range(5, -1, -1):
                if map_data[i][j] != ".":
                    bfs_successful, bombs = bfs(i, j, map_data)
                    if bfs_successful == 1:
                        bomb_set.update(bombs)
        if len(bomb_set) > 0:
            result += 1
            bomb(bomb_set, map_data)
        else:
            break
    return result


def bfs(h: int, w: int, map_data: list) -> Tuple[int, set]:
    positions: set = set()
    q: deque = deque()
    count: int = 1
    q.append((h, w))
    positions.add((h, w))
    while len(q) > 0:
        cur_pos = q.popleft()
        for next_pos in near_pos(cur_pos):
            next_h, next_w = next_pos
            if (
                next_pos not in positions
                and available(next_pos)
                and map_data[h][w] == map_data[next_h][next_w]
            ):
                positions.add(next_pos)
                q.append(next_pos)
                count += 1
    if count >= 4:
        return 1, positions
    return 0, positions


def bomb(positions: set, map_data: list):
    poses: list = sorted(positions, key=lambda x: x[0])
    for pos in poses:
        h, w = pos
        map_data[h][w] = "."
        i: int = h - 1
        while i >= 0 and map_data[i][w] != ".":
            map_data[i + 1][w] = map_data[i][w]
            map_data[i][w] = "."
            i -= 1
    return map_data


def near_pos(pos: Tuple[int, int]):
    h, w = pos
    return [(h - 1, w), (h, w - 1), (h, w + 1), (h + 1, w)]


def available(pos: Tuple[int, int]):
    h, w = pos
    if 0 <= h < 12 and 0 <= w < 6:
        return True
    return False


if __name__ == '__main__':
    def solve():
        map_data: list = [list(input()) for _ in range(12)]
        print(solution(map_data))


    solve()
