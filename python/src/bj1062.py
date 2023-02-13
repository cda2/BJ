from itertools import combinations


def solution(n, k, words):
    if k < 5:
        return 0
    else:
        base_chars = {"a", "n", "t", "i", "c"}
        sets = []
        for word in words:
            word_set = frozenset(word)
            sets.append([word_set - base_chars, 1])
        sets.sort(key=lambda x: len(x[0]), reverse=True)
        delete_impossible(k, sets)
        sets = remove_dup(sets)
        combs = list(combinations(sets, k - 5))
        results = sum_total(combs)
        return get_max(results)


def remove_dup(items):
    result = []
    for i in items:
        is_in = False
        for j in result:
            if i[0] == j[0]:
                j[1] += 1
                is_in = True
        if not is_in:
            result.append(i)
    return result


def get_max(items):
    max_val = 0
    for item in items:
        max_val = max(max_val, item[1])
    return max_val


def delete_impossible(k, sets):
    for i, item in enumerate(sets):
        if len(item[0]) > k - 5:
            del sets[i]


def item_sum(item1, item2):
    return [set_sum(item1[0], item2[0]), item1[1] + item2[1]]


def set_sum(set1, set2):
    return set1 | set2


def sets_sum(sets1, sets2, k):
    result = []
    for i in sets1:
        for j in sets2:
            set_r = item_sum(i, j)
            if set_r not in result and len(set_r[0]) <= k - 5:
                result.append(set_r)
    return result


def sum_total(multiple_sets):
    result = []
    for sets in multiple_sets:
        start = sets[0]
        for i in range(1, len(sets)):
            start = item_sum(start, sets[i])
        result.append(start)
    return result


# n, k = [int(i) for i in input().split()]
# words = [input() for i in range(n)]
# print(solution(n, k, words))

print(solution(3, 6, ["antarctica", "antahellotica", "antacartica"]))
# 2
print(solution(2, 3, ["antaxxxxxxxtica", "antarctica"]))
# 0
print(
    solution(
        9,
        8,
        [
            "antabtica",
            "antaxtica",
            "antadtica",
            "antaetica",
            "antaftica",
            "antagtica",
            "antahtica",
            "antajtica",
            "antaktica",
        ],
    )
)
# 3
print(solution(3, 7, ["antawxtica", "antaytica", "antaztica"]))
# 2
