from sys import stdin


# 점화식 이용
# n이 2일 때 3가지 경우가 있으므로, 우선 n-2 * 3은 기본
# n이 4 이상일 때 생기는 2가지 경우도 더해주어야 함 -> f(n) = 3 * f(n-2) + 2
# 좌우 양 쪽으로 배치가 가능하므로 f(n) = 3 * f(n-2) + 2 * f(n-4) + 2
# n이 8 이상인 경우 미 성립
# 살펴보니 8의 경우 다음과 같은 경우가 존재
# 3 * f(6) + 2 * f(2), f(4) + f(4), 2 (6 이상일 때 항상 생기는 2개 케이스)
# 전체의 합은 3 * f(6) + 2 * f(4) + 2 * f(2) + 2
# 점화식이 3 * f(n-2) + 2 * { f(n-4) + f(n-6) + ... + f(0) } 임을 알 수 있음
# 이 중 뒤의 식을 임시 변수로 저장하면 새로 계산할 필요 없으므로 간결한 코드를 짤 수 있음
def solution(n):
    cache = [0 for i in range(31)]
    cache[2], cache[4] = 3, 11
    sum_value = 0
    if n % 2 != 0:
        return 0
    else:
        if cache[n] == 0:
            for i in range(4, n + 1, 2):
                sum_value += cache[i - 4]
                cache[i] = cache[i - 2] * 3 + sum_value * 2 + 2

    return cache[n]


if __name__ == "__main__":
    print(solution(int(stdin.readline())))
