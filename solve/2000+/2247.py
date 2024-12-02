# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(n):
    """write your logic here"""
    result = 0
    max_limit = int(n**0.5)

    for d in range(2, max_limit):
        d1, d2 = d, n // d
        result += (d2 - 1) * d1
        result += (d1 - 1) * d2

    result += (max_limit - 1) * max_limit

    return result % 1_000_000


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(solve(100), 3150)
    check(solve(12), 2 + 2 + 3 + 2 + 4 + 3 + 2 + 5 + 2 + 3 + 4 + 6)
    check(solve(11), 2 + 2 + 3 + 2 + 4 + 3 + 2 + 5)
    check(solve(10), 2 + 2 + 3 + 2 + 4 + 3 + 2 + 5)
    check(solve(9), 2 + 2 + 3 + 2 + 4 + 3)
    check(solve(8), 2 + 2 + 3 + 2 + 4)
    check(solve(7), 2 + 2 + 3)
    check(solve(6), 2 + 2 + 3)
    check(solve(5), 2)
    check(solve(4), 2)
    check(solve(3), 0)
    check(solve(2), 0)
    check(solve(1), 0)


def main():
    """write your i/o here"""
    a = input_one(int)
    print(solve(a))


test()
main()
