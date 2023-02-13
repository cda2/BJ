from collections import deque, namedtuple
from sys import stdin

Pos: namedtuple = namedtuple("Pos", "row col")
Rot: namedtuple = namedtuple("Rot", "sec dr")


def solution(size: int, apples: set[Pos], drs: deque[Rot]):
    time: int = 0
    snake: deque = deque()
    snake.append(Pos(row=0, col=0))
    dr: int = 1

    while True:
        if len(drs) > 0:
            if drs[0].sec == time:
                rot: Rot = drs.popleft()
                next_dr = -1 if rot.dr == "L" else 1
                dr = (dr + next_dr + 4) % 4

        np: Pos = next_pos(snake, dr)
        if not 0 <= np.row < size or not 0 <= np.col < size or np in snake:
            return time + 1

        if np in apples:
            apples.remove(np)
            move(snake=snake, dr=dr, np=np, eat=True)
        else:
            move(snake=snake, dr=dr, np=np)

        time += 1


def next_pos(snake: deque, dr: int):
    head: Pos = snake[0]
    if dr == 0:
        return Pos(head.row - 1, head.col)
    elif dr == 1:
        return Pos(head.row, head.col + 1)
    elif dr == 2:
        return Pos(head.row + 1, head.col)
    elif dr == 3:
        return Pos(head.row, head.col - 1)


def move(snake: deque, dr: int, np: Pos = None, eat: bool = False):
    if np is None:
        np = next_pos(snake, dr)
    snake.appendleft(np)
    if not eat:
        snake.pop()


def solve():
    n: int = int(stdin.readline())
    k: int = int(stdin.readline())
    apples: set[Pos] = set(
        [pos_mapping(stdin.readline().strip().split()) for _ in range(k)]
    )
    l: int = int(stdin.readline())
    rotates: deque[Rot] = deque(
        [rot_mapping(stdin.readline().strip().split()) for _ in range(l)]
    )
    print(solution(size=n, apples=apples, drs=rotates))


def pos_mapping(inp_data: list[str]) -> Pos:
    row, col = map(int, inp_data)
    return Pos(row=row - 1, col=col - 1)


def rot_mapping(inp_data: list[str]) -> Rot:
    sec, dr = inp_data
    sec = int(sec)
    return Rot(sec=sec, dr=dr)


if __name__ == "__main__":
    solve()
