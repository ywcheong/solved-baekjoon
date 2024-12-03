# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


TEN = range(10)


def hard_solve(n):
    result = [0] * 10
    for x in range(1, n + 1):
        for c in str(x):
            result[int(c)] += 1
    return result


def get_full(k):
    return [k * 10 ** (k - 1)] * 10


def fast_raw(given_num):
    leading, lagging = int(given_num[0]), given_num[1:]
    if len(given_num) == 1:
        return [(1 if i <= leading else 0) for i in TEN]

    result = get_full(len(lagging))
    for i in TEN:
        result[i] *= leading

    for lead in range(leading):
        result[lead] += 10 ** len(lagging)

    result[leading] += int(lagging) + 1
    result_lagging = fast_raw(lagging)

    for i in TEN:
        result[i] += result_lagging[i]
    return result


def fast_solve(n):
    n = str(n)
    L = fast_raw(str(n))
    L[0] -= (10 ** (len(n)) - 1) // 9

    return L


def main():
    """write your code here"""
    n = input_one(str)
    print(" ".join(map(str, (fast_solve(n)))))


main()
