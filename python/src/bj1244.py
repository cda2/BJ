def flip(switch, pos):
    switch[pos] = (switch[pos] + 1) % 2


def male(length, switch, pos):
    origin_pos = pos
    while pos <= length:
        flip(switch, pos - 1)
        pos += origin_pos


def female(length, switch, pos):
    left, right = pos - 1, pos - 1
    while left >= 1 and right < length - 1:
        if switch[left - 1] == switch[right + 1]:
            left -= 1
            right += 1
        else:
            break
    for i in range(left, right + 1):
        flip(switch, i)


if __name__ == "__main__":
    n = int(input())
    switches = [int(i) for i in input().split()]
    students_n = int(input())
    students = [[int(i) for i in input().split()] for j in range(students_n)]

    for student in students:
        gender, pos = student
        if gender == 1:
            male(n, switches, pos)
        elif gender == 2:
            female(n, switches, pos)
    for i, s in enumerate(switches):
        print(str(s), end="\n" if (i + 1) % 20 == 0 else " ")
