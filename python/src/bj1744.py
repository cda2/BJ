from collections import deque
from sys import stdin


def solution(arr):
    q = deque(sorted(arr))
    result = 0
    while len(q) >= 2 and q[-1] > 0 and q[-2] > 0:
        a, b = q.pop(), q.pop()
        result += a * b if a * b >= a + b else a + b
    while len(q) >= 2 and q[0] < 0 and q[1] < 0:
        a, b = q.popleft(), q.popleft()
        result += a * b if a * b >= a + b else a + b
    while len(q) >= 2 and q[0] < 0 and q[1] == 0:
        result += q.popleft() * q.popleft()

    result += sum(q)
    return result


if __name__ == "__main__":
    n = int(stdin.readline())
    array = [int(stdin.readline().strip()) for _ in range(n)]
    print(solution(array))
