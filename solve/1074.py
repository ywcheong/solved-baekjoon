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
def get_order(N, row, column):
    if N == 0:
        return 0

    border = 2 ** (N-1)
    if row < border and column < border:
        # 0-POS
        return get_order(N-1, row, column) + 0 * (border ** 2)
    elif row < border and not(column < border):
        # 1-POS
        return get_order(N-1, row, column-border) + 1 * (border ** 2)
    elif not(row < border) and column < border:
        # 2-POS
        return get_order(N-1, row-border, column) + 2 * (border ** 2)
    else:
        # 3-POS
        return get_order(N-1, row-border, column-border) + 3 * (border ** 2)
    
    
# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(get_order(2, 3, 1), 11)
    equal(get_order(3, 7, 7), 63)
    equal(get_order(1, 0, 0), 0)
    equal(get_order(4, 7, 7), 63)
    equal(get_order(10, 511, 511), 262143)
    equal(get_order(10, 512, 512), 786432)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    N, r, c = input_list(int)
    print(get_order(N, r, c))

# Case-switch
if __name__ == '__main__':
    submit()