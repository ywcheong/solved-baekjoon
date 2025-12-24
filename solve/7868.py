# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
import math


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def parametric_search(cond, lo, hi):
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if cond(mid):  # X O O
            hi = mid
        else:  # X X O
            lo = mid
    return hi


def solve(primes, order):
    p1, p2, p3 = primes

    def count_less(given_q):
        count = 0

        a1 = 0
        while (n1 := p1**a1) <= given_q:
            a2 = 0
            while (n2 := n1 * p2**a2) <= given_q:
                a3 = 0
                while (n3 := n2 * p3**a3) <= given_q:
                    count += 1
                    a3 += 1
                a2 += 1
            a1 += 1

        return count

    def cond(given_q):
        return count_less(given_q) >= order + 1

    return parametric_search(cond, 1, 10**18 + 1)


def test():
    """write your test here"""
    H235 = [2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27]
    for order, q in enumerate(H235):
        assert solve([2, 3, 5], order + 1) == q


def main():
    """write your i/o here"""
    p1, p2, p3, order = input_list(int)
    print(solve([p1, p2, p3], order))


# test()
main()
