from itertools import combinations


def solution(size: int, stats: list):
    result: int = 1000000
    # 쓸모 없어진 방문 확인 dict
    # team_visited: defaultdict = defaultdict(bool)
    # 행렬을 대각선으로 합함
    for i in range(size - 1):
        for j in range(i + 1, size):
            tmp1, tmp2 = stats[i][j], stats[j][i]
            stats[i][j] += tmp2
            stats[j][i] += tmp1
    # return dfs(set(), size, stats, team_visited)
    # set으로 간편하게 difference 계산을 하기 위해 모든 사람을 set에 모아둠
    all_people: frozenset = frozenset(range(size))
    # 가능한 조합 목록, 조합에는 중복이 없으므로 방문 체크할 필요가 없다
    combs: list = list(combinations(range(size), size // 2))
    # (구) 코드의 잔재
    # for index, comb in enumerate(combs):
    #     if index > len(combs) // 2:
    #         break
    # 대략 반절까지만 루프 돌면 됨
    for i in range(len(combs) // 2 + 1):
        # 조합 선택
        comb: tuple = combs[i]
        # 팀 조합 하나를 set으로 만들어 둠
        a_team: frozenset = frozenset(comb)
        # 해당 팀을 전체 구성원에서 빼면 다른 팀이 됨
        b_team: frozenset = all_people.difference(a_team)
        # if a_team not in team_visited and b_team not in team_visited:
        #     team_visited[a_team], team_visited[b_team] = True, True
        # result 값을 각 팀별 스탯 합산하여 뺀 절대값과 비교하여 작은 값으로 저장함
        result = min(
            result, abs(total_stats(a_team, stats) - total_stats(b_team, stats))
        )
    return result


# 팀의 스탯 합을 구하는 용도
def total_stats(team: frozenset, stats: list):
    total_stat: int = 0
    # 이것도 조합 쓰면 간편함
    # 누우면 코드가 번뜩 떠오르는 건 개발자의 특성일까
    for comb in combinations(team, 2):
        y, x = comb
        total_stat += stats[y][x]
    return total_stat


if __name__ == '__main__':
    from sys import stdin


    def solve():
        n: int = int(stdin.readline())
        map_data: list = [
            list(map(int, stdin.readline().strip().split())) for _ in range(n)
        ]
        print(solution(n, map_data))


    solve()
