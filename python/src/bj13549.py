from collections import deque


def solution(n: int, k: int) -> int:
    visited = [False] * 100001
    q = deque()
    q.append((n, 0))
    while len(q) > 0:
        cur_pos, count = q.popleft()
        if cur_pos == k:
            return count
        check_and_push(pos=cur_pos * 2, count=count, visit=visited, queue=q,
                       back=False)
        check_and_push(pos=cur_pos - 1, count=count + 1, visit=visited, queue=q)
        check_and_push(pos=cur_pos + 1, count=count + 1, visit=visited, queue=q)


def check_and_push(pos: int, count: int, visit: list, queue: deque, back=True):
    if 0 <= pos <= 100000 and not visit[pos]:
        visit[pos] = True
        if back:
            queue.append((pos, count))
        else:
            queue.appendleft((pos, count))


if __name__ == '__main__':
    n, k = [int(i) for i in input().split()]
    print(solution(n, k))
