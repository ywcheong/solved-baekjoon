# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys

MOD = 1_000_000_009

def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def presolve():
    """write your logic here"""
    result = [None] * 100_001

    result[1] = (1, 0)
    result[2] = (1, 1)
    result[3] = (2, 2)

    for x in range(4, 100_001):
        o1, e1 = result[x-1]
        o2, e2 = result[x-2]
        o3, e3 = result[x-3]
        result[x] = ((e1 + e2 + e3) % MOD, (o1 + o2 + o3) % MOD)

    return result


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")


def main():
    """write your i/o here"""
    num_testcase = input_one(int)
    result = presolve()
    for _test_id in range(num_testcase):
        o, e = result[input_one(int)]
        print(o, e)


# test()
main()
