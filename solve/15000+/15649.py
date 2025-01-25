# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def solve(population_size, sample_size):
    """write your solution here"""
    def print_sample(sample):
        L = map(str, sample)
        print(" ".join(L))

    def _recursion(sample: list):
        if len(sample) == sample_size:
            print_sample(sample)
            return

        for next_element in population:
            if next_element in sample:
                continue

            _recursion(sample + [next_element])
    
    population = range(1, population_size + 1)
    _recursion([])


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve(1), 1)
    check(solve(2), 2)
    check(solve(3), 3)


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    n, m = input_list(int)
    solve(n, m)


# test()
main()
