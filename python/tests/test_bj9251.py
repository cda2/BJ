from python.src.bj9251 import solution


def test1():
    assert solution("ACAYKP", "CAPCAK") == 4


def test1():
    assert solution(
        "AACGGAACACGCTTTAAGGGCGATGGAATACCGTGGGTTTACCTAAAACTA",
        "AATCTGGCCTATTCTGGGTCAAATGGCGTGAGCAAACATCGTACA",
    ) == 31


def test1():
    assert solution("CAPCK", "AA") == 1


def test1():
    assert solution(
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    ) == 200


def test1():
    assert solution("SKDFHWEODJKSFSDFJK", "WKJSDHFOWEFKJDVKSDF") == 10


def test1():
    assert solution("KJSDFKSDFLKDFJS", "SKDJKFLSKDJFLKSDJF") == 10


def test1():
    assert solution("LKSDJFLKJWPOJSDLKJFSDF", "OISJDKFJLKEJFSLKJDIFJSLDK") == 13
