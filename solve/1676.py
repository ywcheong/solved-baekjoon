# My Solution : https://github.com/ywcheong/solved-baekjoon

# Header
""" import header here """


import sys

input_one = lambda wanted_type: wanted_type(sys.stdin.readline().strip())
input_list = lambda wanted_type: list(map(wanted_type, input().split()))

TESTCASE_ID = 1


def equal(left, right):
    global TESTCASE_ID
    if left == right:
        print(f"Testcase {TESTCASE_ID}: OK ({left} == {right})")
    else:
        print(f"Testcase {TESTCASE_ID}: FAIL ({left} != {right})")
    TESTCASE_ID += 1


# Implementation
""" write code here """
def solve_zero(num):
    pow_5 = num // 5
    pow_25 = num // 25
    pow_125 = num // 125
    return pow_5 + pow_25 + pow_125

# Testing
def test():
    print("WARNING: TEST MODE")

    """ test here """
    # equal(1, 1) -> OK (1 == 1)
    # equal(2, 1) -> FAIL (2 == 1)
    equal(solve_zero(10), 2)
    equal(solve_zero(15), 3)
    equal(solve_zero(3), 0)

    print("TEST DONE")


# Submit
def submit():
    """get input here"""
    print(solve_zero(input_one(int)))


# Case-switch
if __name__ == "__main__":
    # test()
    submit()
