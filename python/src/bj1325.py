from collections import defaultdict, deque
from sys import stdin


def solution(n: int, arr: list) -> list:
    sets: defaultdict = defaultdict(set)
    for a, b in arr:
        sets[b].add(a)

    result: list = []
    max_val: int = -1
    for i in range(1, n + 1):
        bfs_result: int = bfs(pos=i, n=n, nodes=sets)
        if bfs_result > max_val:
            max_val = bfs_result
            result.clear()
            result.append(i)
        elif bfs_result == max_val:
            result.append(i)

    result.sort()
    return result


def bfs(pos: int, n: int, nodes: defaultdict):
    visited: list = [False] * (n + 1)
    q: deque = deque()
    count: int = 0
    visited[pos] = True
    q.append(pos)
    while len(q) > 0:
        pop_pos: int = q.popleft()
        count += 1
        for node in nodes[pop_pos]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
    return count


if __name__ == "__main__":
    n: int
    m: int
    n, m = [int(i) for i in stdin.readline().strip().split()]
    computers: list = [map(int, stdin.readline().strip().split()) for i in
                       range(m)]
    print(*solution(n=n, arr=computers))
