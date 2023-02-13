from sys import stdin


def solution(n):
    cache = [1] * 10
    for i in range(n):
        add = 0
        array = []
        for j in range(-1, -11, -1):
            add += cache[j]
            array.append(add)
        cache += array[::-1]
    return cache[-10] % 10007


if __name__ == "__main__":
    print(solution(int(stdin.readline())))
