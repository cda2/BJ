from collections import deque

ways = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def solution(m, n, arr):
    # 익지 않은 토마토 개수를 세기 위한 변수
    # 배열 속 0의 개수를 셈
    not_changed = 0

    # 방문하였는지를 확인
    # 이미 방문한 노드라면 큐에 삽입하지 않음
    visited = [[False for i in range(m)] for j in range(n)]

    # 큐 초기화
    q = deque()

    # 토마토 창고를 순회
    # 1인 경우 (익지 않은 경우) 큐에 넣어주고 방문 표시
    # 0인 경우 익지 않은 토마토 변수 값 증가
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append([i, j, 0])
                visited[i][j] = True
            elif arr[i][j] == 0:
                not_changed += 1

    # BFS 실행
    return bfs(m, n, arr, visited, q, not_changed)


def bfs(m, n, arr, visited, queue, not_changed):
    # 깊이 변수
    count = 0

    # 큐에 남아 있는 지점이 있는 동안 계속 확인
    while len(queue) > 0:
        # 큐의 맨 앞에서 POP 하여 좌표 값, count 확인
        i, j, count = queue.popleft()

        # 해당 위치 값이 0이라면 (익지 않은 토마토라면)
        if arr[i][j] == 0:
            # 전체 0 개수에서 1을 빼 줌
            not_changed -= 1
        # 해당 위치 값을 1로 설정 (-1인 경우 큐에 삽입되지 않음)
        arr[i][j] = 1

        # 동서남북 좌표 확인하여 가능한 경우 큐에 삽입
        for k, l in ways:
            if check(m, n, arr, visited, i + k, j + l):
                queue.append([i + k, j + l, count + 1])
    # 익지 않은 토마토가 0개가 아니라면 (모두 익어야 하는데 익지 않은 토마토가 있다면) -1 반환
    if not_changed != 0:
        return -1
    return count


# 동서남북 확인하는 함수
def check(m, n, arr, visited, i, j):
    # 좌표 값이 창고 내에 있고
    if 0 <= i <= n - 1 and 0 <= j <= m - 1:
        # 방문한 적이 없다면
        if not visited[i][j]:
            # 방문 표시
            visited[i][j] = True
            # 아직 익지 않은 토마토라면 True 반환, 그 외는 False
            if arr[i][j] == 0:
                return True
            else:
                return False
    return False


if __name__ == "__main__":
    input_m, input_n = [int(i) for i in input().split()]
    arr = [[int(j) for j in input().strip().split()] for i in range(input_n)]
    print(solution(input_m, input_n, arr))

# 8 -1 6 14 0 1 0
print(
    solution(
        6,
        4,
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
        ],
    )
)
print(
    solution(
        6,
        4,
        [
            [0, -1, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
        ],
    )
)
print(
    solution(
        6,
        4,
        [
            [1, -1, 0, 0, 0, 0],
            [0, -1, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0],
            [0, 0, 0, 0, -1, 1],
        ],
    )
)
print(
    solution(
        5,
        5,
        [
            [
                -1,
                1,
                0,
                0,
                0,
            ],
            [0, -1, -1, -1, 0],
            [0, -1, -1, -1, 0],
            [0, -1, -1, -1, 0],
            [0, 0, 0, 0, 0],
        ],
    )
)
print(solution(2, 2, [[1, -1], [-1, 1]]))
print(solution(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 0]]))
print(solution(2, 2, [[1, 1], [1, 1]]))
