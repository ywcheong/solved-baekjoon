# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(liquid_list):
    liquid_list.sort()
    left, right = 0, len(liquid_list) - 1
    ans1, ans2 = left, right

    def liquid_loss(a, b):
        return abs(liquid_list[a] + liquid_list[b])

    while left < right:
        if liquid_loss(ans1, ans2) > liquid_loss(left, right):
            ans1, ans2 = left, right
        
        current_sum = liquid_list[left] + liquid_list[right]
        if current_sum > 0:
            right -= 1
        elif current_sum < 0:
            left += 1
        else:
            right -= 1
            left += 1

    return liquid_list[ans1], liquid_list[ans2]


def main():
    """write your code here"""
    n = input_one(int)
    liquid_list = input_list(int)
    ans1, ans2 = solve(liquid_list)
    print(ans1, ans2)


main()
