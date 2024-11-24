# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from functools import cmp_to_key


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


class Number:
    def __init__(self, s):
        self.s = s

    def __eq__(a, b):
        return int(a.s + b.s) == int(b.s + a.s)
    
    def __lt__(a, b):
        return int(a.s + b.s) > int(b.s + a.s)
    
    def __gt__(a, b):
        return int(a.s + b.s) < int(b.s + a.s)
    
    def __str__(self):
        return self.s


def main():
    """write your code here"""
    size = input_one(int)
    L = input_list(Number)
    L.sort()
    print(int("".join(map(str, L))))

main()
