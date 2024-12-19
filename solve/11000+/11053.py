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
def get_length(L):
    MEMO = [None] * len(L)
    MEMO[-1] = 1

    for start in range(len(L)-2, -1, -1):
        MEMO[start] = 1
        for next in range(start+1, len(L)):
            if L[start] < L[next]:
                MEMO[start] = max(MEMO[start], MEMO[next] + 1)

    return max(MEMO)

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(get_length([4, 5]), 2)
    equal(get_length([5, 4]), 1)
    equal(get_length([5, 5]), 1)
    equal(get_length([5]), 1)
    equal(get_length([5, 4, 3, 2, 1]), 1)
    equal(get_length([5, 4, 3, 2, 3]), 2)
    equal(get_length([1, 2, 3, 4, 5]), 5)
    equal(get_length([1, 2, 3, 4, 3]), 4)
    equal(get_length([10, 20, 10, 30, 20, 50]), 4)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    _ = input()
    L = input_list(int)
    print(get_length(L))

# Case-switch
if __name__ == '__main__':
    submit()