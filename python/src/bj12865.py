def solution(n: int, k: int, arr: list):
    # DP 리스트
    cache: list = [[-1 for i in range(100001)] for i in range(100)]
    return pack(count=0, cur_v=k, cache=cache, arr=arr)


def pack(count: int, cur_v: int, cache: list, arr: list):
    # 더 못 담으면 0 반환
    if count == len(arr):
        return 0
    # 이미 실행한 적 있다면 DP 값 반환
    if cache[count][cur_v] != -1:
        return cache[count][cur_v]
    # 현재 물건을 담지 않는 경우 다음 물건으로 재귀 실행하여 DP 값 저장
    cache[count][cur_v] = pack(count=count + 1, cur_v=cur_v, cache=cache, arr=arr)
    # 현재 물건을 담는 경우 들 수 있는 지 확인
    if cur_v >= arr[count][0]:
        # DP 값에 들기 전 DP 값과 든 후 재귀 실행 결과 값 비교하여 큰 값으로 저장
        cache[count][cur_v] = max(
            cache[count][cur_v],
            pack(count + 1, cur_v - arr[count][0], cache, arr) + arr[count][1],
        )
    # DP 값 반환
    return cache[count][cur_v]


def solve(n: int, k: int, arr: list):
    print(solution(n, k, arr))


if __name__ == '__main__':
    n, k = [int(i) for i in input().split()]
    arr = [[int(i) for i in input().split()] for i in range(n)]
    solve(n=n, k=k, arr=arr)
