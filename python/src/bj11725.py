from collections import deque
from sys import stdin


# BFS
def solution(n, arr):
    nodes = [set() for i in range(n + 1)]
    # 방문했는지 확인
    visited = [False for i in range(n + 1)]
    result = [0 for i in range(n + 1)]
    q = deque()
    # 양 방향 추가
    for a, b in arr:
        nodes[a].add(b)
        nodes[b].add(a)
    # 시작점
    q.append([1, 1])
    while len(q) > 0:
        current, parent = q.popleft()
        # 방문 안한 곳만 BFS 실행
        if not visited[current]:
            visited[current] = True
            # 부모 번호 체크
            result[current] = parent
            for i in nodes[current]:
                q.append([i, current])
    return "\n".join(map(str, result[2:]))

if __name__ == '__main__':

    n = int(stdin.readline())
    arr = [map(int, stdin.readline().strip().split()) for i in range(n - 1)]
    print(solution(n, arr))
