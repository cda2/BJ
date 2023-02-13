def solution(string):
    frequency = [0 for i in range(4)]
    for i in string:
        if i == "w":
            frequency[0] += 1
        elif i == "o":
            frequency[1] += 1
        elif i == "l":
            frequency[2] += 1
        elif i == "f":
            frequency[3] += 1
    if frequency[0] != frequency[1] != frequency[2] != frequency[3]:
        return 0
    i = 0
    while i <= len(string) - 4:
        if string[i] == "w":
            count, tmp = 1, i
            while tmp <= len(string) - 2 and string[tmp + 1] == "w":
                count, tmp = count + 1, tmp + 1
            if (
                string[i: i + count * 4]
                == "w" * count + "o" * count + "l" * count + "f" * count
            ):
                i += count * 4
            else:
                return 0
        else:
            return 0
    if i == len(string):
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(solution(input()))
