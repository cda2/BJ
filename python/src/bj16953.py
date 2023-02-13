from collections import defaultdict, deque


def solution(a: int, b: int) -> int:
    max_val: int = 10 ** 9
    visited: defaultdict = defaultdict(bool)
    q: deque[tuple] = deque()
    visited[a] = True
    q.append((a, 1))
    while len(q) > 0:
        num, count = q.popleft()
        if num == b:
            return count
        else:
            num1: int = op1(num)
            num2: int = op2(num)
            if not visited[num1] and num1 <= max_val:
                q.append((num1, count + 1))
                visited[num1] = True
            if not visited[num2] and num2 <= max_val:
                q.append((num2, count + 1))
                visited[num2] = True
    return -1


def op1(num: int) -> int:
    return num * 2


def op2(num: int) -> int:
    return num * 10 + 1


if __name__ == '__main__':
    from sys import stdin


    def solve():
        a, b = map(int, stdin.readline().strip().split())
        print(solution(a, b))


    solve()
