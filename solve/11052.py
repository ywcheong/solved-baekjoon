# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys

sys.setrecursionlimit(10_000)

PINF = float("inf")
NINF = -PINF


def solve(cards):
    """write your solution here"""
    size = len(cards)
    dp = [0] * (size + 1)
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i - j] + cards[j - 1])
    return dp[size]


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve([1, 5, 6, 7]), 10)
    check(solve([10, 9, 8, 7, 6]), 50)
    check(solve([1, 1, 2, 3, 5, 8, 13, 21, 34, 55]), 55)
    check(solve([5, 10, 11, 12, 13, 30, 35, 40, 45, 47]), 50)
    check(solve([5, 2, 8, 10]), 20)
    check(solve([3, 5, 15, 16]), 18)


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    size = input_one(int)
    L = input_list(int)
    print(solve(L))


# test()
main()
