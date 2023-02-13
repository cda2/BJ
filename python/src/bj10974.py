from itertools import permutations
from typing import Union


# permutations 사용
def solution(n: int) -> Union:
    return permutations(range(1, n + 1), n)


def solve() -> None:
    for i in solution(int(input())):
        print(*i)

if __name__ == "__main__":
    solve()
