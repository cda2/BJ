from sys import stdin


def solution(l: int, p: int, v: int) -> int:
    q, r = divmod(v, p)
    return q * l + (r if r < l else l)


def solve():
    count: int = 1
    while True:
        l, p, v = map(int, stdin.readline().strip().split())
        if (l, p, v) == (0, 0, 0):
            break
        print(f"Case {count}: {solution(l, p, v)}")
        count += 1


if __name__ == "__main__":
    solve()
