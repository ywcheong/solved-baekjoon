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
def get_pow(base, exp, mod):    
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    elif exp % 2 == 0:
        half_pow = get_pow(base, exp//2, mod)
        return (half_pow * half_pow) % mod
    else:
        half_pow = get_pow(base, exp//2, mod)
        return (half_pow * half_pow * base) % mod

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(get_pow(10, 11, 12), 4)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    base, exp, mod = input_list(int)
    print(get_pow(base%mod, exp, mod))

# Case-switch
if __name__ == '__main__':
    submit()