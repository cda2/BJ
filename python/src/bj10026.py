import sys
from copy import deepcopy

sys.setrecursionlimit(10**9)

ways = [[-1, 0], [1, 0], [0, -1], [0, 1]]
rg = ["R", "G"]


# 색맹 기본 값으로 설정
def solution(n, arr, blindness=False):
    # 그룹 수 변수
    count = 0
    # 맵 순회
    for i in range(n):
        for j in range(n):
            # X 발견 시
            if arr[i][j] != "X":
                # 색맹이 아니거나, 색맹이어도 적녹색이 아닌 경우
                if not blindness or (blindness and arr[i][j] not in rg):
                    # 해당 문자열로 DFS 실행
                    dfs(n, arr, i, j, arr[i][j])
                # 아닌 경우 적녹색으로 DFS 실행
                elif arr[i][j] in rg:
                    dfs(n, arr, i, j, rg)
                # 그룹 수 증가
                count += 1
    # 그룹 수 반환
    return count


# DFS 함수
def dfs(n, arr, i, j, chars):
    # 해당 위치 방문 표시
    arr[i][j] = "X"
    # 동서남북으로 순회하면서
    for l, m in ways:
        # 다음 위치가 맵 내에 있고 문자열이 일치하면 (한 그룹이면)
        if check(n, arr, i + l, j + m, chars):
            # 다음 위치를 DFS 실행
            dfs(n, arr, i + l, j + m, chars)


# 맵, 문자열 확인
def check(n, arr, i, j, chars):
    # 한 그룹이거나 맵 속에 있는 경우 True, 그 외 False
    if 0 <= i <= n - 1 and 0 <= j <= n - 1 and arr[i][j] in chars:
        return True
    else:
        return False


if __name__ == "__main__":
    n = int(input())
    arr = [list(input()) for i in range(n)]
    arr1 = deepcopy(arr)

    print(solution(n, arr), solution(n, arr1, True))
