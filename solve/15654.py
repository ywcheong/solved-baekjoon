# THIS SOLUTION IS BASED ON 15650.py
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
def get_perm(L, k):
    return pick(sorted(L), k)

def pick(L, count):
    if count == 0:
        return [tuple()]
    
    result = []
    for i in range(len(L)):
        element = (L[i],)
        remains = pick(L[:i] + L[i+1:], count-1)
        for remain in remains:
            result.append(element + remain)
    
    return result

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(get_perm([4, 5, 2], 1), [
        (2,),
        (4,),
        (5,),
    ])

    equal(get_perm([9, 8, 7, 1], 2), [
        (1, 7),
        (1, 8),
        (1, 9),
        (7, 1),
        (7, 8),
        (7, 9),
        (8, 1),
        (8, 7),
        (8, 9),
        (9, 1),
        (9, 7),
        (9, 8)
    ])

    equal(get_perm([1231, 1232, 1233, 1234], 4), [
        (1231, 1232, 1233, 1234),
        (1231, 1232, 1234, 1233),
        (1231, 1233, 1232, 1234),
        (1231, 1233, 1234, 1232),
        (1231, 1234, 1232, 1233),
        (1231, 1234, 1233, 1232),
        (1232, 1231, 1233, 1234),
        (1232, 1231, 1234, 1233),
        (1232, 1233, 1231, 1234),
        (1232, 1233, 1234, 1231),
        (1232, 1234, 1231, 1233),
        (1232, 1234, 1233, 1231),
        (1233, 1231, 1232, 1234),
        (1233, 1231, 1234, 1232),
        (1233, 1232, 1231, 1234),
        (1233, 1232, 1234, 1231),
        (1233, 1234, 1231, 1232),
        (1233, 1234, 1232, 1231),
        (1234, 1231, 1232, 1233),
        (1234, 1231, 1233, 1232),
        (1234, 1232, 1231, 1233),
        (1234, 1232, 1233, 1231),
        (1234, 1233, 1231, 1232),
        (1234, 1233, 1232, 1231),
    ])

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    n, k = input_list(int)
    L = input_list(int)
    result = get_perm(L, k)
    for perm in result:
        print(" ".join(map(str, perm)))

# Case-switch
if __name__ == '__main__':
    submit()