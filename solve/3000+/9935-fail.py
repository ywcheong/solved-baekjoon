# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    raw = input_one(str)
    explode = input_one(str)
    converted = raw.replace(explode, "")

    while converted != raw:
        converted, raw = converted.replace(explode, ""), converted

    if len(converted) == 0:
        return "FRULA"
    return converted

print(main())
