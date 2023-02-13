from sys import stdin


def solution(size: int, stickers: list[list[int]]):
    dp: list[list[int]] = [[0, 0] for i in range(size)]
    for x in range(size):
        for y in range(2):
            dp[x][y] = max(
                max(get_val(x - 2, dp)) + stickers[y][x],
                get_val(x - 1, dp)[(y + 1) % 2] + stickers[y][x],
            )
    return max(dp[size - 1])


def get_val(x: int, dp: list[list[int]]):
    if x < 0:
        return [0, 0]
    else:
        return dp[x]


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        stickers: list[list[int]] = [
            list(map(int, stdin.readline().strip().split())) for i in range(2)
        ]
        print(solution(n, stickers))

if __name__ == "__main__":
    solve()
