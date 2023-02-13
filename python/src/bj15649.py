from copy import deepcopy

n, m = [int(i) for i in input().split()]


def solve(arr, size, result):
    if len(arr) > 1 and size > 0:
        for i in arr:
            copy = list(deepcopy(arr))
            copy.remove(i)
            new_result = list(deepcopy(result))
            new_result.append(i)
            solve(copy, size - 1, new_result)
    elif len(arr) == 1:
        new_result = [str(i) for i in result]
        new_result.append(str(arr[0]))
        print(" ".join(new_result))
    else:
        print(" ".join([str(i) for i in result]))


if __name__ == '__main__':
    solve(list(range(1, n + 1)), m, [])
