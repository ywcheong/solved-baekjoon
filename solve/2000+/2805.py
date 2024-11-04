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
def get_height(trees, target):
    trees = [0] + sorted(trees)
    low, high = trees[0], trees[-1] # [low, high)

    while high - low >= 2:
        mid = (low + high) // 2
        target_when_mid = sum([(0 if tree < mid else tree - mid) for tree in trees])
        if target_when_mid == target:
            return mid
        elif target_when_mid > target:
            low, high = mid, high
        elif target_when_mid < target:
            low, high = low, mid

    return low

# Testing
def test():
    print("WARNING: TEST MODE")

    equal(get_height([20, 15, 10, 17], 3), 17)
    equal(get_height([20, 15, 10, 17], 7), 15)
    equal(get_height([20, 15, 10, 17], 57), 1)
    equal(get_height([20, 15, 10, 17], 58), 1)
    equal(get_height([20, 15, 10, 17], 59), 0)
    equal(get_height([4, 42, 40, 26, 46], 20), 36)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    N, target = input_list(int)
    trees = input_list(int)
    assert N == len(trees)
    print(get_height(trees, target))

# Case-switch
if __name__ == '__main__':
    submit()