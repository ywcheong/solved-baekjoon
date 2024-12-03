# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(L, days):
    """write your logic here"""
    size = len(L)

    intervals = [None] * (size - days + 1) # interval[i] = sum(L[i:i+days])
    intervals[0] = sum(L[i] for i in range(days)) 
    for i in range(1, size - days + 1):
        # interval[i] = interval[i-1] + (L[i+days-1] - L[i-1])
        intervals[i] = intervals[i-1] + (L[i + days - 1] - L[i - 1])
    
    known_max = intervals[0]
    counter = 1
    for i in range(1, len(intervals)):
        value = intervals[i]
        if value == known_max:
            counter += 1
        elif value > known_max:
            known_max = value
            counter = 1

    return known_max, counter



def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(1 + 1, 2)


def main():
    """write your i/o here"""
    size, days = input_list(int)
    L = input_list(int)
    assert len(L) == size

    known_max, counter = solve(L, days)
    if known_max == 0:
        print("SAD")
    else:
        print(known_max)
        print(counter)


# test()
main()
