# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    n = input_one(int)
    liquid_list = input_list(int)
    liquid_list.sort()  # N lg N

    result = abs(sum(liquid_list[0:3]))
    p0, p1, p2 = 0, 1, 2

    def renew_minimum(left, mid, right):
        nonlocal result, p0, p1, p2
        if (
            abs(new_min := liquid_list[left] + liquid_list[mid] + liquid_list[right])
        ) < result:
            result = abs(new_min)
            p0, p1, p2 = left, mid, right
            # print(f"Renewed: {liquid_list[left]} + {liquid_list[mid]} + {liquid_list[right]} || ", p0, p1, p2)

        return new_min

    for left in range(n - 2):
        mid, right = left + 1, n - 1
        while mid < right:
            current_sum = renew_minimum(left, mid, right)
            if current_sum > 0:
                right -= 1
            elif current_sum < 0:
                mid += 1
            else:
                right -= 1
                mid += 1

    print(liquid_list[p0], liquid_list[p1], liquid_list[p2])


main()
