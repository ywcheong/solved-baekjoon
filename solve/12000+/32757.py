# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(n, k):
    """write your logic here"""
    if k >= n:
        return 0
    if n % 2 == 0:
        return n
    else:
        if k % 2 == 0:
            return n
        else:
            return n - 1


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(solve(4, 1), 4)
    check(solve(4, 2), 4)
    check(solve(4, 3), 4)
    check(solve(4, 4), 0)
    check(solve(5, 1), 4)
    check(solve(5, 2), 5)
    check(solve(5, 3), 4)
    check(solve(5, 4), 5)
    check(solve(5, 5), 0)


def main():
    """write your i/o here"""
    n, k = input_list(int)
    print(solve(n, k))


# test()
main()
