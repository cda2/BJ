from collections import deque


def solution(start: int) -> int:
    q = deque()
    q.append([start, 0])
    count = 0

    while len(q) > 0:
        num, c = q.popleft()
        if num == 1:
            count = c
            break
        if num % 3 == 0:
            q.append([num // 3, c + 1])
        if num % 2 == 0:
            q.append([num // 2, c + 1])
        q.append([num - 1, c + 1])

    return count


if __name__ == "__main__":
    x = int(input())
    print(solution(start=x))
