def fibo(n):
    a, b = 0, 1
    for i in range(n):
        tmp = (a + b) % 1000000000
        a = b
        b = tmp
    return a


def solution(n):
    result = 0
    fibo_result = fibo(abs(n))
    if n < 0:
        if n % 2 == 0:
            result = -1
        else:
            result = 1
    elif fibo_result > 0:
        result = 1
    return "\n".join(map(str, [result, fibo_result]))


if __name__ == "__main__":
    print(solution(int(input())))
