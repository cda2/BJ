from collections import deque
from sys import stdin


# BFS
def solution(n, a, b, m, arr):
    visited = [False for i in range(n + 1)]
    next_pos = [set() for i in range(n + 1)]
    q = deque()
    # 양 방향으로 넣어줌
    for x, y in arr:
        next_pos[x].add(y)
        next_pos[y].add(x)
    q.append([a, 0])
    visited[a] = True
    # 각 루프마다 count + 1
    while len(q) > 0:
        cur_pos, count = q.popleft()
        if cur_pos == b:
            return count
        for i in next_pos[cur_pos]:
            if not visited[i]:
                visited[i] = True
                q.append([i, count + 1])
    return -1


if __name__ == "__main__":
    n = int(stdin.readline())
    a, b = map(int, stdin.readline().strip().split())
    m = int(stdin.readline())
    arr = [map(int, stdin.readline().strip().split()) for i in range(m)]

    print(solution(n, a, b, m, arr))
