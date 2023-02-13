from collections import deque
from sys import stdin


# 체스 말 이동 방향
def next_pos():
    return [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]


# BFS
def solution(size, cur_y, cur_x, end_y, end_x):
    visited = [[False for i in range(size)] for j in range(size)]
    visited[cur_y][cur_x] = True
    q = deque()
    q.append([cur_y, cur_x, 0])
    while len(q) > 0:
        y, x, count = q.popleft()
        # 목적지 도착 시 결과 값 반화
        if y == end_y and x == end_x:
            return count
        # 이동 가능한 위치인 경우 큐에 추가
        for ny, nx in next_pos():
            next_y, next_x = y + ny, x + nx
            if (
                0 <= next_y < size
                and 0 <= next_x < size
                and not visited[next_y][next_x]
            ):
                visited[next_y][next_x] = True
                q.append([next_y, next_x, count + 1])
    return -1


if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        l = int(stdin.readline())
        cy, cx = map(int, stdin.readline().strip().split())
        ey, ex = map(int, stdin.readline().strip().split())
        print(solution(l, cy, cx, ey, ex))
