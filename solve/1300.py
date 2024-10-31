# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


# Let C = {a * b | a, b in {1, ..., n}}
# Let cond(mid) := |{x | x in C and x <= mid}| >= target
# cond(-1) == False
# cond(n*n+1) == True

# |{x | x in C and x <= target}| >= target
# 


def parametric_search(cond, lo, hi):
    # lg(num_limit ^ 2) => lg(num_limit)
    while lo + 1 < hi:  # X ? O
        mid = (lo + hi) // 2
        if cond(mid):  # X O O
            hi = mid
        else:  # X X O
            lo = mid
    return hi


def main():
    """write your code here"""
    num_limit, target_index = input_one(int), input_one(int)

    def cond(mid):
        count = 0
        x = 1
        while x**2 <= mid:
            count += min(mid // x, num_limit)
            x += 1
        count = 2 * count - (x-1)**2
        return count >= target_index

    print(parametric_search(cond, -1, target_index))


main()
