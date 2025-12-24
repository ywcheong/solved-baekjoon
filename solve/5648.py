# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def solve(x):
    """write your solution here"""
    return x


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(flip_num(123), 321)
    check(flip_num(120), 21)
    check(solve(2), 2)
    check(solve(3), 3)


def flip_num(x):
    result = 0
    power = 0

    while x > 0:
        head, tail = x // 10, x % 10
        x, power, result = \
            head, power + 1, result * 10 + tail
    
    return result


def flip_list(nums):
    return [flip_num(x) for x in nums]


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    init_list = input_list(int)
    size = init_list[0]
    init_size = len(init_list) - 1

    nums = flip_list(init_list[1:])
    while len(nums) < size:
        nums.extend(flip_list(input_list(int)))

    nums.sort()
    for x in nums:
        print(x)


# test()
main()
