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
UP, DOWN = 0, 1

def batch_solve_maximum_value(stickers_list):
    return [solve_maximum_value(stickers) for stickers in stickers_list]

def solve_maximum_value(stickers):
    length = len(stickers[UP])

    # Solve simple cases
    if length == 1:
        return max(stickers[UP][0], stickers[DOWN][0])

    # Prepare for recurrence relation solving
    up, down, no = [None] * 2, [None] * 2, [None] * 2
    up[0], down[0], no[0] = stickers[UP][0], stickers[DOWN][0], 0
    
    for i in range(1, length):
        up[i%2]   = stickers[UP][i] + max(down[(i-1)%2], no[(i-1)%2])
        down[i%2] = stickers[DOWN][i] + max(up[(i-1)%2], no[(i-1)%2])
        no[i%2]   = max(up[(i-1)%2], down[(i-1)%2], no[(i-1)%2])

    return max(up[(length-1)%2], down[(length-1)%2])

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(solve_maximum_value([
        [50, 10, 100, 20, 40],
        [30, 50, 70, 10, 60],
    ]), 260)

    equal(solve_maximum_value([
        [10, 30, 10, 50, 100, 20, 40],
        [20, 40, 30, 50, 60, 20, 80],
    ]), 290)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    testcase_count = int(input())
    stickers_list = [None] * testcase_count
    for i in range(testcase_count):
        stickers_list[i] = [None, None]
        _ = input()
        stickers_list[i][0] = input_list(int)
        stickers_list[i][1] = input_list(int)
    
    result = batch_solve_maximum_value(stickers_list)
    print("\n".join(map(str, result)))

# Case-switch
if __name__ == '__main__':
    submit()