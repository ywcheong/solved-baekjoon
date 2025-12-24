# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    size = input_one(int)
    L = input_list(int)

    known_max = 0
    current_height, current_kill = L[0], 0

    for i in range(1, size):
        if L[i] > current_height:
            known_max = max(known_max, current_kill)
            current_height, current_kill = L[i], 0
        else:
            current_kill += 1

    known_max = max(known_max, current_kill)
    print(known_max)


main()
