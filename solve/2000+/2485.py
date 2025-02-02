# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a


def get_spacing(nums):
    spacing = 0
    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        spacing = gcd(diff, spacing)
    return spacing


def get_empty_count(nums, spacing):
    start, end = nums[0], nums[-1]
    return (end - start) // spacing + 1 - len(nums)


def solve(nums):
    """write your solution here"""
    spacing = get_spacing(nums)
    return get_empty_count(nums, spacing)


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve([1, 3, 7, 13]), 3)
    check(solve([2, 6, 12, 18]), 5)
    check(solve(list(range(2, 100001, 2)) + [100001]), 49999)


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
