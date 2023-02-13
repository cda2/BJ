from sys import stdin


def solution(string):
    result = 0
    for i, s in enumerate(string.split("-")):
        tmp = 0
        for t in s.split("+"):
            tmp += int(t)
        if i == 0:
            result += tmp
        else:
            result -= tmp

    return result


if __name__ == "__main__":
    print(solution(stdin.readline().strip()))
