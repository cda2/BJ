def solution(document, string):
    count = 0
    i = 0
    while i <= len(document) - len(string):
        if document[i] == string[0]:
            is_same = True
            for j in range(1, len(string)):
                if document[i + j] != string[j]:
                    is_same = False
            if is_same:
                count += 1
                i += len(string)
            else:
                i += 1
        else:
            i += 1

    return count


if __name__ == "__main__":
    print(solution(input(), input()))
