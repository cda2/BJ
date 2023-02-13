def solution(a, b):
    big, small = max(a, b), min(a, b)
    return int(factorial(big) / (factorial(small) * factorial(big - small)))


def factorial(num):
    result = 1
    for f in range(1, num + 1):
        result *= f
    return result


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = [int(num) for num in input().split()]
        print(solution(n, m))
