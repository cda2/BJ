from collections import defaultdict


def solution(cur_pos: tuple[int, int], cur_dir: int, map_data: list[list[int]]):
    result: int = 0
    visited: defaultdict = defaultdict(bool)
    while True:
        # 현재 좌표 추출
        cy, cx = cur_pos

        # 방문한 적 없는 경우 방문 표시 후 값을 2로 변경하고 영역 카운팅 + 1
        if not visited[cur_pos]:
            visited[cur_pos] = True
            map_data[cy][cx] = 2
            result += 1

        # 다음 위치들, 벽이 존재하므로 인덱스 에러 걱정은 없다
        next_positions: list[tuple[int, int]] = next_poses(cy, cx)
        # 이후 제자리인지 아닌지 확인하기 위해 현재 위치를 이전 위치로 저장
        prev_pos = cur_pos

        # 4 방향 확인해야 함.
        # 현재 방향을 매 번 그냥 바꾸어 주면 되는데,
        # 다음 방향 = (현재 방향 - 1) % 4로 구하면 다음 좌표를 간편하게 구할 수 있음
        for i in range(4):
            cur_dir = (cur_dir - 1) % 4
            # 틀은 방향의 좌표 정보 저장
            nxt_pos = next_positions[cur_dir]
            ny, nx = nxt_pos

            # 해당 방향 칸이 청소 가능하면
            if map_data[ny][nx] == 0:
                # 이동, 어차피 위에서 청소시키므로 문제 없음
                cur_pos = nxt_pos
                # break 문으로 for문 탈출해서 방향 유지
                break

        # 만약 4 방향 다 검사를 했는데 진행 불가능하면 (아까 저장 값과 좌표가 같으면)
        if prev_pos == cur_pos:
            # 마지막 방향의 반대 방향 좌표를 저장 (뒤로 이동)
            back_pos = next_positions[(cur_dir - 2) % 4]
            by, bx = back_pos
            # 해당 좌표 값이 벽이면 아예 청소 종료
            if map_data[by][bx] == 1:
                break
            # 벽은 아닌 경우 1칸 뒤로 이동
            else:
                cur_pos = back_pos

    return result


def next_poses(py: int, px: int):
    return [(py - 1, px), (py, px + 1), (py + 1, px), (py, px - 1)]


if __name__ == "__main__":
    from sys import stdin


    def solve():
        n, m = map(int, stdin.readline().strip().split())
        r, c, d = map(int, stdin.readline().strip().split())
        map_info: list = [
            list(map(int, stdin.readline().strip().split())) for _ in range(n)
        ]
        print(solution((r, c), d, map_info))


    solve()
