from sys import stdin


def solution(arr1, arr2):
    tmp = 0
    for i, v in enumerate(arr1):
        arr1[i] += tmp
        tmp += v
    result = []
    for a, b in arr2:
        result.append(arr1[b - 1] - (arr1[a - 2] if a - 2 >= 0 else 0))
    return "\n".join(map(str, result))

if __name__ == '__main__':
    n, m = map(int, stdin.readline().strip().split())
    n_arr = list(map(int, stdin.readline().strip().split()))
    m_arr = [map(int, stdin.readline().strip().split()) for i in range(m)]
    print(solution(n_arr, m_arr))
