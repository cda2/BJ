import sys

input = sys.stdin.readline


def solution(n, arr):
    # DP 리스트
    cache = [0 for i in range(n + 1)]
    # DP의 1 값을 받은 배열의 첫 값으로 초기화
    cache[1] = arr[0]
    # 1-n 까지 dp 함수 실행
    for i in range(1, n + 1):
        dp(cache, arr, i)
    # 결과 값 반환
    return cache[n]


def dp(cache, arr, index):
    # 계산이 되어 있지 않다면 (조건 상 1 이상이므로 0이라면 계산이 되어 있지 않음.)
    if cache[index] == 0:
        # DP 리스트에서 BEST 값들을 더함
        # 예를 들어 다음과 같음

        # DP[4] = DP[1] + DP[3] = DP[1] + DP[4-1]
        # DP[4] = DP[2] + DP[2] = DP[2] + DP[4-2]
        # DP[4] = DP[4]

        # DP[5] = DP[1] + DP[4] = DP[1] + DP[5-1]
        # DP[5] = DP[2] + DP[3] = DP[2] + DP[5-2]
        # DP[5] = DP[5]

        # 자세히 보면 index를 2로 나눈 경우까지만 순회 후 index 값을 추가하면 됨 (인덱스 안 넘는 선에서)
        # 해당 목록 중에서 max 값만 추출하면 끝

        # index // 2 까지만 순회하여 리스트에 저장
        tmp = [cache[index - i] + cache[i] for i in range(1, index // 2 + 1)]
        # 인덱스 에러 나지 않게 처리
        if len(arr) >= index:
            # 인덱스 값 추가
            tmp.append(arr[index - 1])
        # 최대 값 저장
        cache[index] = max(tmp)
        return cache[index]


if __name__ == "__main__":
    # 문제 입력
    n, arr = int(input().strip()), [int(i) for i in input().strip().split()]
    print(solution(n, arr))
