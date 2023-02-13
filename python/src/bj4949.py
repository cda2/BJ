def solution(string):
    answer = []
    braces = ["[", "]", "(", ")"]
    bomb = ["[]", "()"]
    for char in string:
        # print(answer, char)
        if char in braces:
            answer.append(char)
        if len(answer) >= 2:
            while "".join(answer[-2:]) in bomb:
                for i in range(2):
                    answer.pop()
    return "yes" if len(answer) == 0 else "no"


if __name__ == "__main__":
    while True:
        text = input()
        if text == ".":
            break
        print(solution(text))
