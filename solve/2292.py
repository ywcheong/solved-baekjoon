# My Solution : https://github.com/ywcheong/solved-baekjoon

import math, sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    n = input_one(int)
    k = math.ceil(((12 * n - 3) ** 0.5 - 3) / 6) + 1
    print(k)


main()
