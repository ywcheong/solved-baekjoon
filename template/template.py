# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def solve(x):
    """write your solution here"""
    return x


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve(1), 1)
    check(solve(2), 2)
    check(solve(3), 3)


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    x = input_one(int)
    print(solve(x))


test()
main()
