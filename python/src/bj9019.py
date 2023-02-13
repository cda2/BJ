from collections import deque
from sys import stdin


def solution(a: int, b: int) -> str:
    q = deque()
    route = [False for i in range(10000)]
    push(num=a, prev=a, command="", queue=q, route=route)
    while len(q) > 0:
        pop = q.popleft()
        if pop == b:
            result = deque()
            while route[b][0] != a:
                result.appendleft(route[b][1])
                b = route[b][0]
            result.appendleft(route[b][1])
            return "".join(result)
        else:
            dr, sr, lr, rr = d(pop), s(pop), l(pop), r(pop)
            # 함수화하면 무조건 시간초과 뜨는 게 말이야 방구야
            # push(num=dr, prev=pop, command='D', queue=q, route=route)
            # push(num=sr, prev=pop, command='S', queue=q, route=route)
            # push(num=lr, prev=pop, command='L', queue=q, route=route)
            # push(num=rr, prev=pop, command='R', queue=q, route=route)

            if route[dr] is False:
                push(num=dr, prev=pop, command="D", queue=q, route=route)
            if route[sr] is False:
                push(num=sr, prev=pop, command="S", queue=q, route=route)
            if route[lr] is False:
                push(num=lr, prev=pop, command="L", queue=q, route=route)
            if route[rr] is False:
                push(num=rr, prev=pop, command="R", queue=q, route=route)


def push(num: int, prev: int, command: str, queue: deque, route: list):
    # if route[num] is False:
    #     route[num] = (prev, command)
    #     queue.append(num)i
    route[num] = (prev, command)
    queue.append(num)


def d(num: int) -> int:
    return (num * 2) % 10000


def s(num: int) -> int:
    return num - 1 if num > 0 else 9999


def l(num: int) -> int:
    quot, remain = divmod(num, 1000)
    return remain * 10 + quot


def r(num: int) -> int:
    quot, remain = divmod(num, 10)
    return remain * 1000 + quot


if __name__ == "__main__":
    t = int(stdin.readline())
    for _ in range(t):
        n1, n2 = [int(i) for i in stdin.readline().strip().split()]
        print(solution(n1, n2))
