# My Solution : https://github.com/ywcheong/solved-baekjoon

# Header
""" import header here """


import sys

input = lambda: sys.stdin.readline().strip()
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


def get_maximum_sum(triangle):
    # memo[depth][i] = Max sum from (0, 0) -> (level, i)
    memo = [[None] * (depth + 1) for depth in range(len(triangle))]
    memo[0][0] = triangle[0][0]

    for depth in range(1, len(triangle)):
        # depth: 1, [0, 1]: 2)
        for i in range(depth + 1):
            if i == 0:  # leftmost
                memo[depth][0] = memo[depth - 1][0] + triangle[depth][0]
            elif i == depth:  # rightmost
                memo[depth][-1] = memo[depth - 1][-1] + triangle[depth][-1]
            else:
                memo[depth][i] = (
                    max(memo[depth - 1][i - 1], memo[depth - 1][i])
                ) + triangle[depth][i]

    return max(memo[-1])


# Testing
def test():
    print("WARNING: TEST MODE")

    """ test here """
    # equal(1, 1) ->
    equal(
        get_maximum_sum(
            [
                [7],
                [3, 8],
                [8, 1, 0],
                [2, 7, 4, 4],
                [4, 5, 2, 6, 5],
            ]
        ), 30
    )

    print("TEST DONE")


# Submit
def submit():
    """get input here"""
    N = int(input())
    triangle = [None] * N
    for i in range(N):
        triangle[i] = input_list(int)
    print(get_maximum_sum(triangle))

# Case-switch
if __name__ == "__main__":
    submit()
