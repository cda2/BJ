from python.src.bj11052 import solution


def test1():
    assert solution(10, [1, 10, 1, 1, 1, 1]) == 50


def test2():
    assert solution(5, [10, 9, 8, 7, 6]) == 50


def test3():
    assert solution(10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) == 55


def test4():
    assert solution(4, [1, 5, 6, 7]) == 10


def test5():
    assert solution(10, [5, 10, 11, 12, 13, 30, 35, 40, 45, 47]) == 50


def test6():
    assert solution(4, [5, 2, 8, 10]) == 20


def test7():
    assert solution(4, [3, 5, 15, 16]) == 18


def test8():
    assert solution(10, [1, 100, 160, 1, 1, 1, 1, 1, 1, 1]) == 520
