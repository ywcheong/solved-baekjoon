# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def solve(L):
    """write your solution here"""
    size = len(L)
    for num_correct in range(size, -1, -1):
        if num_correct == len(list(filter(lambda x: x == num_correct, L))):
            return num_correct
    return -1


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve([0, 3, 1, 3, 2, 3]), 3)
    check(solve([0, 1, 2, 3]), 1)
    check(solve([1, 1]), 0)
    check(solve([0]), -1)


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    size = input_one(int)
    L = input_list(int)
    print(solve(L))


# test()
main()
