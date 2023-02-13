from sys import stdin


def solution(array: list) -> int:
    money: int = 0

    max_val: int = array[-1]
    for v in reversed(array[:-1]):
        if v > max_val:
            max_val = v
        elif v < max_val:
            money += max_val - v
    return money


def solve():
    t: int = int(stdin.readline())
    for _ in range(t):
        n: int = int(stdin.readline())
        array: list[int] = list(map(int, stdin.readline().split()))
        print(solution(array))


if __name__ == '__main__':
    solve()
