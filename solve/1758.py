# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(tips):
    """write your logic here"""
    tips.sort()
    result = 0
    for i, tip in enumerate(reversed(tips)):
        result += max(0, tip - i)
    return result


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(solve([3, 3, 3, 3]), 6)
    check(solve([3, 2, 3]), 5)
    check(solve([7, 8, 6, 9, 10]), 30)
    check(solve([1, 1, 1, 1, 2]), 2)
    check(solve([1, 2, 3]), 4)


def main():
    """write your i/o here"""
    size = input_one(int)
    tips = [None] * size
    for i in range(size):
        tips[i] = input_one(int)
    print(solve(tips))


# test()
main()
