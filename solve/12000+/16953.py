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
def get_count(target, given):
    count = 1
    while target < given:
        if given % 10 == 1:
            given //= 10
        elif given % 2 == 0:
            given //= 2
        else:
            return -1
        count += 1

    if target == given:
        return count
    return -1

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(get_count(2, 162), 5)
    equal(get_count(4, 42), -1)
    equal(get_count(100, 40021), 5)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    target, given = input_list(int)
    print(get_count(target, given))

# Case-switch
if __name__ == '__main__':
    submit()