# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(L):
    """write your logic here"""
    sum_value = sum(L)
    max_value = max(L)

    return min(
        sum_value,
        2 * (sum_value - max_value) + 1
    )


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(solve([1, 1, 3]), 5)
    check(solve([3, 5]), 7)
    check(solve([2, 2, 2, 3]), 9)


def main():
    """write your i/o here"""
    size = input_one(int)
    L = input_list(int)
    assert size == len(L)

    print(solve(L))


# test()
main()
