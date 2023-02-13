from sys import stdin


def solution(n):
    cache = [1, 1, 1]
    while len(cache) < n:
        cache.append(cache[-2] + cache[-3])
    return cache[-1]


if __name__ == "__main__":
    n = int(stdin.readline())
    for i in range(n):
        print(solution(int(stdin.readline())))
