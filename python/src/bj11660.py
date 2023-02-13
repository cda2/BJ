import sys
from copy import deepcopy

# 입력 속도 증가
input = sys.stdin.readline


# 계산된 행렬에서 정답 계산
def solution(arr, ax, ay, bx, by):
    ax, ay, bx, by = ax - 1, ay - 1, bx - 1, by - 1
    # 구하는 영역 한 칸 왼쪽의 맨 아래
    nx1, ny1 = ax - 1, by
    # 영역 한칸 위 맨 오른쪽
    nx2, ny2 = bx, ay - 1
    # 영역 오른쪽 아래
    right_bottom = arr[bx][by]
    # 좌표 값이 영역 밖이라면 0 처리
    right_up = arr[nx1][ny1] if nx1 >= 0 else 0
    left_bottom = arr[nx2][ny2] if ny2 >= 0 else 0
    # 영역 좌상단(-1, -1) 위치도 동일하게 0 처리
    left_up = arr[nx1][ny2] if nx1 >= 0 and ny2 >= 0 else 0
    # 우측 하단 - 우측 상단 - 좌측 하단 + 좌측 상단 값이 정답
    return right_bottom - right_up - left_bottom + left_up


# 행렬 계산
def new_map(n, arr):
    result = deepcopy(arr)
    for i in range(n):
        tmp = 0
        for j in range(n):
            if i > 0:
                result[i][j] += result[i - 1][j]
            if j > 0:
                tmp += arr[i][j - 1]
                result[i][j] += tmp
    return result


if __name__ == '__main__':
    n, m = [int(i) for i in input().strip().split()]
    arr = [[int(j) for j in input().strip().split()] for i in range(n)]
    new_map = new_map(n, arr)
    for i in range(m):
        x1, y1, x2, y2 = [int(j) for j in input().split()]
        print(solution(new_map, x1, y1, x2, y2))
