from sys import stdin


def solution(tape_l: int, positions: list[int]) -> int:
    positions.sort()
    count: int = 0
    pos: int = 0
    next_pos: int = pos
    if len(positions) == 1:
        return 1
    while pos < len(positions):
        if next_pos >= len(positions):
            count += 1
            break
        elif abs(positions[pos] - positions[next_pos]) + 1 > tape_l:
            pos = next_pos
            count += 1
        else:
            next_pos += 1
    return count


def solve():
    n, l = map(int, stdin.readline().strip().split())
    leak_points: list = list(map(int, stdin.readline().strip().split()))
    print(solution(l, leak_points))


if __name__ == "__main__":
    solve()
