# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def solve(L):
    """write your solution here"""
    size = len(L)
    if 1 <= size <= 2:
        return sum(L)

    iend, iiend = [None] * size, [None] * size
    iend[0:2] = [L[0], L[1]]
    iiend[0:2] = [0, L[0] + L[1]]

    for i in range(2, size):
        iend[i] = max(iend[i - 2], iiend[i - 2]) + L[i]
        iiend[i] = max(iend[i - 1], iend[i - 2]) + L[i]

    return max(iend[size - 1], iiend[size - 1])


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve([10, 20, 15, 25, 10, 20]), 75)


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    size = input_one(int)
    nums = [None] * size
    for i in range(size):
        nums[i] = input_one(int)
    print(solve(nums))


# test()
main()
