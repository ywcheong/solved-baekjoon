# My Solution : https://github.com/ywcheong/solved-baekjoon

# Header
''' import header here '''


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
''' write code here '''
sys.setrecursionlimit(10000)
NEGATIVE_INFINITE = float("-inf")
WEIGHT_INDEX, VALUE_INDEX = 0, 1

def solve_value(thing_list, max_weight):
    '''Given the list of things = (weight, value), and max weight that bag can hold, find max values can be packed'''
    # memo[w] := solve(thing_list, w)
    memo = [0] * (max_weight+1)

    for i in range(len(thing_list)):
        for w in range(max_weight, thing_list[i][WEIGHT_INDEX]-1, -1):
            # Updating dp[w]
            #                       V Containing thing_list[i]
            memo[w] = max(memo[w], memo[w-thing_list[i][WEIGHT_INDEX]] + thing_list[i][VALUE_INDEX])
            #             ^ Skipping thing_list[i]
        pass # Invariant: dp[w] contains optimal Knapsack of capacity w, for thing_list[:i+1] at here

    return memo[max_weight]

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(solve_value([
        (6, 13),
        (4, 8),
        (3, 6),
        (5, 12),
    ], 7), 14)

    equal(solve_value([
        (9, 100),
        (2, 21),
        (2, 21),
        (2, 21),
        (2, 21),
        (2, 21),
    ], 10), 105)

    equal(solve_value([
        (9, 106),
        (2, 21),
        (2, 21),
        (2, 21),
        (2, 21),
        (2, 21),
    ], 10), 106)

    equal(solve_value([
        (2, 5),
    ], 13), 5)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    N, max_weight = input_list(int)
    thing_list = [None] * N
    for i in range(N):
        thing_list[i] = input_list(int)
    print(solve_value(thing_list, max_weight))

# Case-switch
if __name__ == '__main__':
    # test()
    submit()