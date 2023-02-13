from sys import stdin


# 대충 set으로 입력하면 해결
def solution(n, actual_arr, m, find_arr):
    result = []
    for data in find_arr:
        if data in actual_arr:
            result.append("1")
        else:
            result.append("0")
    return " ".join(result)

if __name__ == "__main__":
    n = int(stdin.readline().strip())
    arr = set(map(int, stdin.readline().strip().split()))
    m = int(stdin.readline().strip())
    arr1 = map(int, stdin.readline().strip().split())

    print(solution(n, arr, m, arr1))
