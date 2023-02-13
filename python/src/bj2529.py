def solution(string: list) -> list:
    # DFS 로 결과 값 저장하는 배열
    result: list = list()
    # 방문 확인
    visited: list = [False] * 10
    # DFS 실행
    dfs(perm="", braces=string, visit=visited, rst=result)
    return result


# 문제 입력시 부등호를 str 타입으로 넘기면 매 번 복사 발생, list로 변경
def dfs(perm: str, braces: list, visit: list, rst: list) -> None:
    # 순열 생성이 완료된 경우 결과 목록에 추가하고 함수 종료
    if len(perm) == len(braces) + 1:
        rst.append(perm)
        return None
    # DFS, 백트래킹으로 방문 표시하면서 순열 생성 가능한 경우만 진입
    # 확인해보니 K 값이 9가 들어와도 만들어지는 순열이 약 1만개 이하이므로 시간 상 양호함
    for i in range(10):
        if visit[i]:
            continue
        elif len(perm) == 0 or check(
            brace=braces[len(perm) - 1], prev_num=int(perm[-1]), next_num=i
        ):
            visit[i] = True
            dfs(perm=perm + str(i), braces=braces, visit=visit, rst=rst)
            visit[i] = False


# 괄호 확인하여 조건 만족 안하면 False, 그 외는 True
def check(brace: str, prev_num: int, next_num: int) -> bool:
    if brace == "<":
        if prev_num >= next_num:
            return False
    elif brace == ">":
        if prev_num <= next_num:
            return False
    return True


# K 값을 안 써도 어차피 len 함수로 처리 가능, O(1)
def solve(k: int = int(input()), string: list = input().split()):
    result: list = solution(string)
    print(result[-1])
    print(result[0])


if __name__ == "__main__":
    solve()
