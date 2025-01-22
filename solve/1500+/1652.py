# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys

EMPTY = "."
BLOCK = "X"


def solve(room):
    """write your solution here"""
    return solve_garo(room), solve_sero(room)


def solve_garo(room):
    size = len(room)
    count = 0

    for i in range(size):
        space = 0
        for j in range(size):
            if room[i][j] == EMPTY:
                space += 1
                if space == 2:
                    count += 1
            else:
                space = 0

    return count


def solve_sero(room):
    size = len(room)
    count = 0

    for j in range(size):
        space = 0
        for i in range(size):
            if room[i][j] == EMPTY:
                space += 1
                if space == 2:
                    count += 1
            else:
                space = 0

    return count


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    size = input_one(int)
    room = [None for _ in range(size)]
    for i in range(size):
        room[i] = list(input_one(str))

    garo, sero = solve(room)
    print(garo, sero)


main()
