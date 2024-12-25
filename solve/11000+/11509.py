# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque


def solve(heights):
    """write your solution here"""
    count = 0
    arrows = dict()

    for h in heights:
        if h in arrows and arrows[h] > 0:
            arrows[h] -= 1
            arrows[h - 1] = arrows.get(h - 1, 0) + 1
        else:
            count += 1
            arrows[h - 1] = arrows.get(h - 1, 0) + 1

    return count
    



def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve([2, 1, 5, 4, 3]), 2)
    check(solve([1, 2, 3, 4, 5]), 5)
    check(solve([4, 5, 2, 1, 4]), 3)
    check(solve([3, 3, 2, 2, 2]), 3)
    check(solve([3, 3, 3, 2, 2]), 3)
    check(solve([3, 3, 2, 2]), 2)
    check(solve([3, 2, 2, 2]), 3)
    check(solve([3, 3, 3, 2]), 3)
    check(solve(list(range(1, 1_000_001))), 1_000_000)
    check(solve(list(range(1_000_000, 0, -1))), 1)


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    size = input_one(int)
    heights = input_list(int)
    
    assert len(heights) == size
    print(solve(heights))


# test()
main()
