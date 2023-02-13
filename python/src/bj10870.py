def solution(n):
    dp = [0, 1]
    if n < 2:
        return dp[n]
    else:
        while len(dp) - 1 < n:
            dp.append(dp[-1] + dp[-2])
        return dp[-1]


if __name__ == "__main__":
    print(solution(int(input())))
