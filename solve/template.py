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
def get_cost(street):
    N = len(street)
    MEMO = [[None]*3 for _ in range(N)]
    MEMO[0] = list(street[0])

    for i in range(1, N):
        MEMO[i][0] = street[i][0] + min(MEMO[i-1][1], MEMO[i-1][2])
        MEMO[i][1] = street[i][1] + min(MEMO[i-1][0], MEMO[i-1][2])
        MEMO[i][2] = street[i][2] + min(MEMO[i-1][0], MEMO[i-1][1])

    return min(MEMO[-1])

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    equal(get_cost([
        (26, 40, 83),
        (49, 60, 57),
        (13, 89, 99),
    ]), 96)

    equal(get_cost([
        (1, 100, 100),
        (100, 1, 100),
        (100, 100, 1),
    ]), 3)

    equal(get_cost([
        (1, 100, 100),
        (100, 100, 100),
        (1, 100, 100),
    ]), 102)

    equal(get_cost([
        (30, 19, 5),
        (64, 77, 64),
        (15, 19, 97),
        (4, 71, 57),
        (90, 86, 84),
        (93, 32, 91),
    ]), 208)

    equal(get_cost([
        (71, 39, 44),
        (32, 83, 55),
        (51, 37, 63),
        (89, 29, 100),
        (83, 58, 11),
        (65, 13, 15),
        (47, 25, 29),
        (60, 66, 19),
    ]), 253)
    

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    N = int(input())
    street = [None] * N
    for i in range(N):
        street[i] = input_list(int)
    print(get_cost(street))

# Case-switch
if __name__ == '__main__':
    submit()