def palindrome_check(string):
    if string == string[::-1]:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    arr = []
    while True:
        string = input()
        if string == "0":
            break
        arr.append(string)

    for string in arr:
        palindrome_check(string)
