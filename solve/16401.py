# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))



def parametric_search(cond, lo, hi):
    # O O O ... O O X X ...
    while lo + 1 < hi:
        mid = (lo + hi) // 2    # O ? X
        if cond(mid):           # O O X
            lo = mid
        else:                   # O X X
            hi = mid
    return lo   # [O] X


def main():
    """write your code here"""
    num_person, _ = input_list(int)
    snacks = input_list(int)

    def cond(give_length):
        count = 0
        for snack in snacks:
            count += (snack // give_length)
        return count >= num_person
    
    if not cond(1):
        print(0)
    else:
        print(parametric_search(cond, 1, 1_000_000_001))


main()
