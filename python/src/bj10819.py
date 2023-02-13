from itertools import permutations


def solution(n: int, arr: list) -> int:
    result: int = 0
    for perm in permutations(arr, n):
        result = max(result, get_val(perm=perm))
    return result


def get_val(perm: tuple) -> int:
    result: int = 0
    for i in range(len(perm) - 1):
        result += abs(perm[i] - perm[i + 1])
    return result


def solve(n: int = int(input()), arr=None):
    if arr is None:
        arr = sorted(list(map(int, input().split())))
    print(solution(n, arr))

if __name__ == "__main__":
    solve()
