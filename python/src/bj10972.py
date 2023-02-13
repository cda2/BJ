def solution(num, arr):
    for i in range(num - 1, 0, -1):
        if arr[i] > arr[i - 1]:
            for j in range(n - 1, i - 1, -1):
                if arr[j] > arr[i - 1]:
                    arr[j], arr[i - 1] = arr[i - 1], arr[j]
                    return " ".join(map(str, arr[:i] + sorted(arr[i:])))
    return -1


if __name__ == "__main__":
    n = int(input())
    array = [int(i) for i in input().strip().split()]
    print(solution(n, array))
