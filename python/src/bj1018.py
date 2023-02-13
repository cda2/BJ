from sys import stdin


# 브루트 포스로 풀어도 큰 문제 없음
def solution(n, m, arr):
    result = 2500
    map1, map2 = [
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
    ], [
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
    ]
    for i in range(n - 7):
        for j in range(m - 7):
            count1, count2 = 0, 0
            for x in range(8):
                for y in range(8):
                    if arr[i + x][j + y] != map1[x][y]:
                        count1 += 1
                    if arr[i + x][j + y] != map2[x][y]:
                        count2 += 1
            result = min(count1, count2, result)

    return result


if __name__ == "__main__":
    n, m = map(int, stdin.readline().strip().split())
    chess_map = [stdin.readline().strip() for i in range(n)]
    print(solution(n, m, chess_map))
