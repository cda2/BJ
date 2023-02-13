from sys import stdin


def solution(array: list[int]):
    dp: list[int] = [10000] * len(array)
    dp[0] = 0

    for i in range(len(array)):
        for j in range(array[i], 0, -1):
            if i + j < len(array) and dp[i + j] > dp[i] + 1:
                dp[i + j] = dp[i] + 1

    return -1 if dp[-1] == 10000 else dp[-1]


def solve():
    n: int = int(stdin.readline())
    array: list[int] = list(map(int, stdin.readline().strip().split()))
    print(solution(array=array))


if __name__ == "__main__":
    solve()
