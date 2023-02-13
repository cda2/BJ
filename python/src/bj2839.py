def solution(n):
    q, r = n // 5, n % 5
    for i in range(q, -1, -1):
        tmp = n - 5 * i
        if tmp % 3 == 0:
            return i + tmp // 3
    return -1


if __name__ == "__main__":
    print(solution(int(input())))
