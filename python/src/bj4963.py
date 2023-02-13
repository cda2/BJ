def solution(w, h, arr):
    # 섬의 개수 결과 값 변수
    count = 0
    # 맵을 순회하면서
    for i in range(h):
        for j in range(w):
            # 빈 공간을 찾으면 DFS 실행
            if arr[i][j] == 1:
                dfs(w, h, arr, i, j)
                # 섬 개수 증가
                count += 1
    return count


# DFS 함수
def dfs(w, h, arr, i, j):
    # 방문한 곳은 0으로 표시
    arr[i][j] = 0
    # 주변 8칸 순회
    for l in range(-1, 2):
        for m in range(-1, 2):
            # 맵 내에 있고 값이 1이면 DFS 실행
            if check(w, h, arr, i + l, j + m):
                dfs(w, h, arr, i + l, j + m)


# 방문 가능한지 확인
def check(w, h, arr, i, j):
    if 0 <= i <= h - 1 and 0 <= j <= w - 1 and arr[i][j] == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        w, h = [int(i) for i in input().split()]
        if w == 0 and h == 0:
            break
        arr = [[int(i) for i in input().split()] for j in range(h)]
        print(solution(w, h, arr))
