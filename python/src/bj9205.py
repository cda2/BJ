from collections import defaultdict, deque
from sys import stdin
from typing import List, Tuple


def solution(
    s_pos: Tuple[int, int], e_pos: Tuple[int, int], conv_list: List[Tuple[int, int]]
) -> str:
    if bfs(s_pos=s_pos, e_pos=e_pos, conv_list=conv_list):
        return "happy"
    else:
        return "sad"


def bfs(
    s_pos: Tuple[int, int], e_pos: Tuple[int, int], conv_list: List[Tuple[int, int]]
) -> bool:
    visit: defaultdict = defaultdict(bool)
    q: deque = deque()
    visit[s_pos] = True
    q.append(s_pos)
    while len(q) > 0:
        cur_pos: Tuple[int, int] = q.popleft()
        if distance(cur_pos, e_pos) <= 1000:
            return True
        for next_pos in conv_list:
            if not visit[next_pos] and distance(cur_pos, next_pos) <= 1000:
                visit[next_pos] = True
                q.append(next_pos)
    return False


def distance(pos_a: Tuple[int, int], pos_b: Tuple[int, int]) -> int:
    return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])

if __name__ == "__main__":
    t: int = int(stdin.readline())
    for i in range(t):
        n: int = int(stdin.readline())
        start_pos: tuple = tuple(map(int, stdin.readline().strip().split()))
        conv_positions: list = [
            tuple(map(int, stdin.readline().strip().split())) for _ in range(n)
        ]
        end_pos: tuple = tuple(map(int, stdin.readline().strip().split()))
        print(
            solution(s_pos=start_pos, e_pos=end_pos, conv_list=conv_positions))
