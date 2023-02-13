def solution(n, arr):
    charset = [set() for i in range(50)]
    result = ""
    for string in arr:
        for i, char in enumerate(string):
            charset[i].update(char)
    for i in charset:
        if len(i) == 1:
            result += i.pop()
        elif len(i) > 1:
            result += "?"
        else:
            break

    return result


if __name__ == "__main__":
    n = int(input())
    arr = [input() for i in range(n)]
    print(solution(n, arr))

# print(solution(3, ['config.sys', 'config.inf', 'configures']))
