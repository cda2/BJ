def solution(r, c, array):
    # 남 / 북 / 서 / 동
    ways = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # 큐 대신 중복 비허용 셋 사용
    q = set()
    # 초기값 추가
    # set 내에는 set이 들어갈 수 없으므로 frozenset으로 만들어 immutable 상태로 변경
    q.add((0, 0, 1, frozenset(array[0][0])))

    # 결과 값 변수
    result = 1

    # 큐에 원소가 있는 경우
    while len(q) > 0:
        # pop
        i, j, depth, chars = q.pop()
        # 결과 값 비교하여 갱신
        result = max(result, depth)

        # 4방향 검사
        for way in ways:
            # 다음 행 열 좌표 값 설정
            next_row, next_col = i + way[0], j + way[1]
            # 인덱스 초과하지 않으면
            if 0 <= next_row < r and 0 <= next_col < c:
                # 다음 문자 확인
                next_char = array[next_row][next_col]
                # 해당 문자가 사용된 적 없는 경우
                if next_char not in chars:
                    # pop한 frozenset을 set으로 변경
                    cpy_chars = set(chars)
                    # set에 char 추가
                    cpy_chars.add(next_char)
                    # set을 다시 frozenset으로 변경
                    cpy_chars = frozenset(cpy_chars)
                    # 큐에 다음 좌표 추가
                    q.add((next_row, next_col, depth + 1, cpy_chars))
    return result


if __name__ == "__main__":
    input_m, input_n = [int(i) for i in input().split()]
    arr = [input() for i in range(input_m)]
    print(solution(input_m, input_n, arr))
