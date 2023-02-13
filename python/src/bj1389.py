from collections import defaultdict, deque
from sys import stdin


def solution(user_n: int, r_list: list):
    relations: defaultdict = defaultdict(set)
    for a, b in r_list:
        relations[a].add(b)
        relations[b].add(a)
    result: list = [(i, bfs(start=i, relation=relations)) for i in
                    range(1, user_n + 1)]
    return min(result, key=lambda x: x[1])[0]


def bfs(start: int, relation: defaultdict) -> int:
    visited: defaultdict = defaultdict(bool)
    visited[start] = True
    q: deque = deque()
    q.append((start, 0))
    result: int = 0
    while len(q) > 0:
        cur_pos, count = q.popleft()
        result += count
        for next_pos in relation[cur_pos]:
            if not visited[next_pos]:
                visited[next_pos] = True
                q.append((next_pos, count + 1))
    return result


def solve():
    n: int
    m: int
    n, m = map(int, stdin.readline().strip().split())
    rel_list: list = [map(int, stdin.readline().strip().split()) for i in
                      range(m)]
    print(solution(user_n=n, r_list=rel_list))


if __name__ == "__main__":
    solve()
