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
def get_perm(n, k):
    return pick(1, n, k)

def pick(start, end, count):
    if count == 0:
        return [tuple()]

    # if (end - start + 1) == count: early stop
    if end - start + 1 == count:
        return [tuple(range(start, end+1))]
    # (start,) + (start+1, end, count-1)
    # (start+1, end, count)

    result = pick(start+1, end, count-1)
    for i in range(len(result)):
        result[i] = (start,) + result[i]
    result.extend(pick(start+1, end, count))
    return result

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(get_perm(3, 1), [
        (1,),
        (2,),
        (3,),
    ])

    equal(get_perm(4, 2), [
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 3), 
        (2, 4),
        (3, 4)
    ])

    equal(get_perm(4, 4), [
        (1, 2, 3, 4)
    ])

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    n, k = input_list(int)
    result = get_perm(n, k)
    for perm in result:
        print(" ".join(map(str, perm)))

# Case-switch
if __name__ == '__main__':
    submit()