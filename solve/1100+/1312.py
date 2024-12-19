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
def solve_number(numerator, denominator, digit_location):
    numerator %= denominator
    while digit_location > 0:
        digit_now = (10 * numerator) // denominator
        numerator = 10 * numerator - (digit_now * denominator)
        digit_location -= 1
    return digit_now

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> OK (1 == 1)
    # equal(2, 1) -> FAIL (2 == 1)
    equal(solve_number(25, 5, 100), 0)
    equal(solve_number(24, 5, 100), 0)
    equal(solve_number(25, 3, 1000000), 3)
    equal(solve_number(26, 3, 100), 6)
    equal(solve_number(25, 7, 5), 2)
    equal(solve_number(4, 7, 5), 2)
    

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    numerator, denominator, digit_location = input_list(int)
    print(solve_number(numerator, denominator, digit_location))

# Case-switch
if __name__ == '__main__':
    # test()
    submit()