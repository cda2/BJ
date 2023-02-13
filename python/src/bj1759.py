from itertools import combinations
from sys import stdin


# 조합 문제
# 자음 2개 이상, 모음 1개 이상인지만 체크해서 결과 반환하면 끝
# 메모리도 많이 주고, 귀찮으니 combinations 사용
def solution(l, c, arr):
    combs = [list(i) for i in list(combinations(sorted(arr), l))]
    result = []
    # 각 조합마다
    for comb in combs:
        # 자음 모음 개수 확인하는 변수
        cons, vowel = 0, 0
        # 각 글자마다
        for char in comb:
            # 자음인 경우 자음 변수 값 1 증가
            if char not in {"a", "e", "i", "o", "u"}:
                cons += 1
            # 모음인 경우 모음 변수 값 1 증가
            else:
                vowel += 1
        # 자음 >= 2, 모음 >= 1 인 경우만 결과 목록에 추가
        if cons >= 2 and vowel >= 1:
            result.append("".join(comb))
    # newline 문자열에 join 하여 반환
    return "\n".join(result)


if __name__ == "__main__":
    l, c = map(int, stdin.readline().strip().split())
    chars = stdin.readline().strip().split()

    print(solution(l, c, chars))
