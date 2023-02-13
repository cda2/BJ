from collections import deque
from sys import stdin


# BFS로 해결
def solution(v, e, arr):
    # 한 정점에 연결된 다른 정점들 정보
    # 중복 방지 등을 위해 set 사용
    nodes = [set() for i in range(v + 1)]
    # 각 그래프 클래스를 확인
    # 방문 여부도 확인하기 위해 -1로 설정
    # 방문한 vertex라면 0이나 1의 상태가 되어야 함
    graph_class = [-1 for i in range(v + 1)]
    # 큐 초기화
    q = deque()
    # 노드 연결
    for n1, n2 in arr:
        nodes[n1].add(n2)
        nodes[n2].add(n1)
    # 일단 1~N까지 순회하면서 정점 하나를 넣어 줌
    # 하나를 큐에 넣고 graph_class의 값을 수정해 준 후 break
    # loop_index 변수는 -1이 graph_class에 남아있는지 확인하기 위함
    # ( 검사되지 않은 vertex가 있는지 확인하기 위함 )
    loop_index = 1
    for index, node in enumerate(nodes):
        if len(node) > 0:
            q.append([index, 0])
            graph_class[index] = 0
            loop_index = index
            break
    # BFS를 실행
    result = bfs(q, nodes, graph_class)
    # BFS를 실행해도 남아있는 vertex가 있을 수 있음
    # 이는 모든 정점이 연결되어 있지 않은 경우가 있을 수 있기 때문
    # 예를 들어 다음과 같은 입력이 들어오는 경우,
    # 1
    # 6 3
    # 1 2
    # 3 4
    # 5 6
    # 1-2, 3-4, 5-6 만 연결되어있고, 이 세 노드는 연결되어있지 않음
    # 만약 맨 앞의 첫 vertex만 큐에 삽입 후 이 그래프를 검사하는 경우 NO가 정답이 됨
    # 그러나 실제로는 정답은 YES이고, 3-4, 5-6이 검사 되지 않았기 때문임
    # 이를 위해 -1이 있는지 확인해주고, 있으면 해당 vertex에 연결된 노드들을 검사 후 체크
    # 다만 NO 인 경우 추가로 검사할 필요는 없음
    while loop_index < v + 1 and result != "NO":
        if graph_class[loop_index] == -1:
            q.append([loop_index, 0])
            graph_class[loop_index] = 0
            result = bfs(q, nodes, graph_class)
        loop_index += 1
    # 결과 값 반환
    return result


# BFS 함수
def bfs(q, nodes, graph_class):
    while len(q) > 0:
        # POP
        vertex, cls = q.popleft()
        for i in nodes[vertex]:
            # 방문한 적 없는 노드인 경우
            if graph_class[i] == -1:
                # 1을 더하고 2로 나눈 나머지를 저장
                # cls가 -1 인 경우 0
                # cls가 0 인 경우 1
                # cls가 1 인 경우 0
                graph_class[i] = (cls + 1) % 2
                # 큐에 삽입
                q.append([i, (cls + 1) % 2])
            # 클래스가 같은 경우 (이분 그래프가 아닌 경우)
            elif graph_class[i] == cls:
                # 바로 NO 반환
                return "NO"
    # 순회가 끝나면 무조건 YES
    return "YES"


if __name__ == "__main__":
    k = int(stdin.readline())
    for _ in range(k):
        v, e = map(int, stdin.readline().strip().split())
        arr = [map(int, stdin.readline().strip().split()) for i in range(e)]
        print(solution(v, e, arr))
