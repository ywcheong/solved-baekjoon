# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from typing import List

LEFT_MODE, RIGHT_MODE = 0, 1
PINF = float("inf")

def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(L: List[int], min_diff: int):
    """write your logic here"""
    if min_diff == 0:
        return 0

    L.sort()
    size = len(L)
    L += [PINF]

    left, right = 0, 0
    result = PINF

    while left < size:
        move_mode = None

        if right == size:
            move_mode = LEFT_MODE
        elif L[right] - L[left] >= min_diff:
            move_mode = LEFT_MODE
        else:
            move_mode = RIGHT_MODE

        if move_mode == LEFT_MODE:
            left += 1
        else:
            right += 1

        if left < size and right < size and (diff := L[right] - L[left]) >= min_diff:
            result = min(result, diff)

    return result


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(1 + 1, 2)


def main():
    """write your i/o here"""
    size, min_diff = input_list(int)
    L = [None] * size
    for i in range(size):
        L[i] = input_one(int)
    print(solve(L, min_diff))


# test()
main()
