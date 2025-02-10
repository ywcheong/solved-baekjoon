# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def solve(x):
    """write your solution here"""
    count = 0
    while x > 0:
        if x % 2 == 1:
            count += 1
        x //= 2
    return count


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve(23), 4)
    check(solve(32), 1)
    check(solve(64), 1)
    check(solve(48), 2)


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    length = input_one(int)
    print(solve(length))


# test()
main()
