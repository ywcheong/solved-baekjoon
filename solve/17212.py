# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(a):
    """write your logic here"""
    result = [None] * (a + 1)
    result[0] = 0

    for i in range(1, len(result)):
        result[i] = result[i - 1] + 1
        for k in [2, 5, 7]:
            if i - k >= 0:
                result[i] = min(result[i], result[i - k] + 1)
        
    return result[-1]



def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(solve(12), 2)
    check(solve(17), 3)
    check(solve(21), 3)
    check(solve(0), 0)
    check(solve(1), 1)


def main():
    """write your i/o here"""
    a = input_one(int)
    print(solve(a))


# test()
main()
