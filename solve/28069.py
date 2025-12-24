# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(goal, remain_step):
    """write your logic here"""
    if goal <= 3:
        return goal <= remain_step
    
    while remain_step > 0:
        k = goal // 3
        if goal % 3 != 2:
            goal -= k
        else:
            goal -= 1

        remain_step -= 1
        
        if goal <= 3:
            return goal <= remain_step
        
    return False



def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(solve(5, 2), False)
    check(solve(42, 10), True)


def main():
    """write your i/o here"""
    goal, step = input_list(int)
    print("minigimbob" if solve(goal, step) else "water")


# test()
main()
