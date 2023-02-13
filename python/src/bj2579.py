from collections import deque


def solution(number: int) -> int:
    q = deque()
    for i in range(number):
        q.append(int(input()))
    dp = deque()

    if number >= 1:
        dp.append(q[0])
    if number >= 2:
        dp.append(max(q[0] + q[1], q[1]))
    if number >= 3:
        dp.append(max(q[0] + q[2], q[1] + q[2]))
        for i in range(3, number):
            dp.append(max(dp[i - 3] + q[i - 1] + q[i], dp[i - 2] + q[i]))
    return dp.pop()


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
