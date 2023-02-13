def solution(n, arr):
    result = [0 for i in range(n + 2)]
    for i, item in enumerate(arr):
        if i == 0:
            continue
        for j in range(0, n - i + 1):
            pos, value = i + j, result[i]
            next_pos, next_value = pos + arr[pos][0], value + arr[pos][1]
            if next_pos <= n + 1:
                result[next_pos] = max(result[next_pos], next_value)
    return max(result)


if __name__ == '__main__':
    from sys import stdin

    n = int(stdin.readline())
    array = [[0, 0]]
    for i in range(n):
        array.append([int(i) for i in stdin.readline().strip().split()])
    print(solution(n, array))
