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
def get_pos(L):
    M = sorted(L)
    rank = dict()

    new_rank = 0
    for i in range(len(M)):
        x = M[i]
        if x not in rank:
            rank[x] = new_rank
            new_rank += 1
    
    return [rank[x] for x in L]


# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    equal(get_pos([2, 4, -10, 4, -9]), [2, 3, 0, 3, 1])
    equal(get_pos([1000, 999, 1000, 999, 1000, 999]), [1,0,1,0,1,0])

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    _ = input()
    L = input_list(int)
    print(" ".join(map(str, get_pos(L))))

# Case-switch
if __name__ == '__main__':
    submit()