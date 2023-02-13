from collections import defaultdict, deque
from sys import stdin


def solution(num: int, arr: list, input_v: int) -> tuple:
    node_dict = defaultdict(list)
    dfs_result = []
    dfs_visited = [False] * (num + 1)
    for begin, end in arr:
        node_dict[begin].append(end)
        node_dict[end].append(begin)
    for value in node_dict.values():
        value.sort()
    dfs(node=node_dict, visit=dfs_visited, cur_vertex=input_v,
        result=dfs_result)

    bfs_result = bfs(num=num, node=node_dict, vertx=input_v)
    return " ".join(list(map(str, dfs_result))), " ".join(
        list(map(str, bfs_result)))


def dfs(node: defaultdict, visit: list, cur_vertex: int, result: list) -> None:
    if not visit[cur_vertex]:
        visit[cur_vertex] = True
        result.append(cur_vertex)
        for vertex in node[cur_vertex]:
            dfs(node, visit, vertex, result)


def bfs(num: int, node: defaultdict, vertx: int) -> list:
    bfs_result = []
    bfs_visited = [False] * (num + 1)
    q = deque()
    q.append(vertx)
    while len(q) > 0:
        pop_node = q.popleft()
        if not bfs_visited[pop_node]:
            bfs_visited[pop_node] = True
            bfs_result.append(pop_node)
            for vertex in node[pop_node]:
                q.append(vertex)
    return bfs_result


if __name__ == "__main__":
    n, m, v = [int(i) for i in stdin.readline().strip().split()]
    nodes = [[int(i) for i in stdin.readline().strip().split()] for j in
             range(m)]
    results = solution(n, nodes, v)
    for i in results:
        print(i)
