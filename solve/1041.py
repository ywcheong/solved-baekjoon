# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def get_m1(dice):
    return min(dice)


def get_m2(dice):
    a, b, c, d, e, f = dice
    m2_list = [
        a + b, b + f, f + e, e + a,
        a + d, d + f, f + c, c + a,
        d + b, b + c, c + e, e + d
    ]

    return min(m2_list)


def get_m3(dice):
    a, b, c, d, e, f = dice
    m3_list = [
        a + e + d, a + d + b, a + b + c, a + c + e,
        f + e + d, f + d + b, f + b + c, f + c + e
    ]

    return min(m3_list)


def get_m5(dice):
    return sum(dice) - max(dice)


def solve(dice, n):
    """write your solution here"""
    if n == 1:
        return get_m5(dice)

    m1 = get_m1(dice)
    m2 = get_m2(dice)
    m3 = get_m3(dice)

    top = 4 * m3 + 4 * (n - 2) * m2 + (n - 2) ** 2 * m1
    side = (n - 1) * m2 + (n - 1) * (n - 2) * m1
    
    # print(f"m1={m1} m2={m2} m3={m3} top={top} side={side} result={top+4*side}")

    return top + 4 * side


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve([1, 2, 3, 4, 5, 6], 1), 15)
    check(solve([1, 2, 3, 4, 5, 6], 2), 36)
    check(solve([1, 2, 3, 4, 5, 6], 3), 69)
    check(solve([50, 50, 50, 50, 50, 50], 1000000), 250000000000000)
    check(solve([1, 1, 1, 1, 50, 1], 10), 500)



def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    n = input_one(int)
    dice = input_list(int)
    print(solve(dice, n))


# test()
main()
