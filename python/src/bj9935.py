def solution(string, bomb):
    bomb_len = len(bomb)
    answer = []

    for char in string:
        answer += char
        answer_len = len(answer)
        while (
            answer_len > 0
            and answer[-1] == bomb[-1]
            and "".join(answer[max(answer_len - bomb_len, 0):]) == bomb
        ):
            for _ in range(bomb_len):
                answer.pop()
            answer_len = len(answer)

    return "FRULA" if len(answer) == 0 else "".join(answer)


if __name__ == "__main__":
    s = input().strip()
    b = input().strip()
    print(solution(s, b))
