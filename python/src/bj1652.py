def solution(n, arr):
    width_count, height_count = 0, 0
    map_data = [[[True, True] for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "X":
                map_data[i][j] = [False, False]
    for i in range(n):
        for j in range(n):
            if i < n - 1 and map_data[i][j][0] and map_data[i + 1][j][0]:
                tmp = i
                while tmp <= n - 1 and map_data[tmp][j][0]:
                    map_data[tmp][j][0] = False
                    tmp += 1
                height_count += 1
            if j < n - 1 and map_data[i][j][1] and map_data[i][j + 1][1]:
                tmp = j
                while tmp <= n - 1 and map_data[i][tmp][1]:
                    map_data[i][tmp][1] = False
                    tmp += 1
                width_count += 1

    return str(width_count) + " " + str(height_count)


if __name__ == "__main__":
    n = int(input())
    arr = [input() for i in range(n)]
    print(solution(n, arr))
