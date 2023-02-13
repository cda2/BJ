from collections import deque


def sub(pos1, pos2):
    return [pos1[0] - pos2[0], pos1[1] - pos2[1]]


def add(pos1, pos2):
    return [pos1[0] + pos2[0], pos1[1] + pos2[1]]


class N13460:
    def __init__(self):
        self.max_y, self.max_x = [int(i) for i in input().strip().split()]

        # game_map = ['#' for i in range(m)] * n
        self.game_map = []
        self.red_pos, self.blue_pos, self.hole_pos = None, None, None
        self.move_able_dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.queue = deque()
        self.visited = [
            [
                [[False] * self.max_x for i in range(self.max_y)]
                for j in range(self.max_x)
            ]
            for k in range(self.max_y)
        ]

        # reset to input
        for i in range(self.max_y):
            row = list(input().strip())
            self.game_map.append(row)
            if "R" in row:
                self.red_pos = [i, row.index("R")]
            if "B" in row:
                self.blue_pos = [i, row.index("B")]
            if "O" in row:
                self.hole_pos = [i, row.index("O")]

        self.visited[self.red_pos[0]][self.red_pos[1]][self.blue_pos[0]][
            self.blue_pos[1]
        ] = True
        self.queue.appendleft([self.red_pos, self.blue_pos, 0])

    def moved_pos(self, pos, move_pos):
        count = 0
        p = pos
        while (
            self.game_map[add(p, move_pos)[0]][add(p, move_pos)[1]] != "#"
            and self.game_map[p[0]][p[1]] != "O"
        ):
            p = add(p, move_pos)
            count += 1
        is_end = self.game_map[p[0]][p[1]] == "O"
        return [is_end, p, count]

    def get_answer(self):
        while len(self.queue) > 0:
            red_pos, blue_pos, depth = self.queue.pop()
            if depth >= 10:
                break
            for d in self.move_able_dirs:
                is_red_end, next_red, red_count = self.moved_pos(
                    pos=red_pos, move_pos=d
                )
                is_blue_end, next_blue, blue_count = self.moved_pos(
                    pos=blue_pos, move_pos=d
                )
                if not is_blue_end:
                    if is_red_end:
                        return depth + 1
                    if next_red == next_blue:
                        if red_count > blue_count:
                            next_red = sub(next_red, d)
                        else:
                            next_blue = sub(next_blue, d)
                    if not self.visited[next_red[0]][next_red[1]][next_blue[0]][
                        next_blue[1]
                    ]:
                        self.queue.appendleft([next_red, next_blue, depth + 1])
                        self.visited[next_red[0]][next_red[1]][next_blue[0]][
                            next_blue[1]
                        ] = True
        return -1

if __name__ == '__main__':
    prob = N13460()
    print(prob.get_answer())
