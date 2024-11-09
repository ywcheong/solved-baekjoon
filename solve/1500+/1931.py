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
def get_count(times):
    times = sorted(times, key=lambda t: (t[1], t[0]))
    result = [times[0]]

    for time in times[1:]:
        start, end = time
        if result[-1][1] <= start:
            result.append(time)

    return len(result)

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(get_count([(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]), 4)
    equal(get_count([(2, 2), (3, 3), (2, 3), (1, 11)]), 3)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    N = int(input())
    times = [None] * N
    for i in range(N):
        times[i] = input_list(int)
    print(get_count(times))


# Case-switch
if __name__ == '__main__':
    submit()