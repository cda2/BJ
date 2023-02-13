from collections import deque


def solution(node: int, node_cnt: int) -> int:
    q = deque()
    nodes = [set() for i in range(node)]
    affected = [False] * node
    for i in range(node_cnt):
        start, end = [int(i) for i in input().split()]
        nodes[start - 1].add(end - 1)
        nodes[end - 1].add(start - 1)

    affected[0] = True
    q.append(0)
    while len(q) > 0:
        point = q.popleft()
        for node in nodes[point]:
            if not affected[node]:
                affected[node] = True
                q.append(node)

    count = 0
    for i in range(1, node):
        if affected[i]:
            count += 1

    return count


if __name__ == "__main__":
    n = int(input())
    nc = int(input())
    print(solution(n, nc))
