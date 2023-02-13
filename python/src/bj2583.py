from sys import setrecursionlimit, stdin

setrecursionlimit(10**7)


# 이동 가능한 위치
def near_pos():
    return [[-1, 0], [1, 0], [0, -1], [0, 1]]


# DFS 사용
def solution(m, n, k, arr):
    # 모눈 종이 정보, 정상 영역은 1, 아닌 경우 0
    paper = [[1 for i in range(m)] for j in range(n)]
    for ax, ay, bx, by in arr:
        for i in range(ax, bx):
            for j in range(ay, by):
                paper[i][j] = 0
    result = 0
    # 각 영역의 넓이 체크
    # 리스트는 mutable 하므로, -1 인덱스로 접근해서 증가시키면 간편하고 속도도 빠름
    count = []
    visited = [[False for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if paper[i][j] == 1:
                # 리스트 맨 뒤에 영역 넓이를 0으로 추가
                count.append(0)
                # DFS로 영역 표시 및 넓이 체크
                dfs(paper, visited, m, n, i, j, count)
                result += 1
    # 문제 조건에 따라서 정렬하여 답 제시
    return "\n".join([str(result), " ".join(map(str, sorted(count)))])


def dfs(paper, visit, m, n, x, y, count):
    paper[x][y] = -1
    visit[x][y] = True
    # 영역 넓이 증가
    count[-1] += 1
    for nx, ny in near_pos():
        next_x, next_y = x + nx, y + ny
        # 다음 위치가 이동 가능한 경우 DFS 재귀 실행
        if (
            0 <= next_x < n
            and 0 <= next_y < m
            and not visit[next_x][next_y]
            and paper[next_x][next_y] == 1
        ):
            dfs(paper, visit, m, n, x + nx, y + ny, count)

if __name__ == "__main__":
    m, n, k = map(int, stdin.readline().strip().split())
    arr = [map(int, stdin.readline().strip().split()) for i in range(k)]

    print(solution(m, n, k, arr))
