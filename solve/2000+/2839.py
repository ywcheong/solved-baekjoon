# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    n = input_one(int)

    result = 0
    while n % 5 != 0:
        n -= 3
        result += 1

    if n < 0:
        return -1
    else:
        return result + (n // 5)


print(main())
