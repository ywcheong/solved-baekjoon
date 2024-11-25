# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(a):
    """write your logic here"""
    return None


def test():
    """write your test here"""
    assert 1 == 1


def main():
    """write your i/o here"""
    a = input_one(int)
    print(solve(a))


test()
main()
