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
def divide_range(interval):
    start, end = interval
    if end - start == 1:
        raise Exception("cannot divide single interval")
    return (start, (start+end)//2), ((start+end)//2, end)

def check_range(board, xrange, yrange):
    color = board[xrange[0]][yrange[0]]
    for x in range(*xrange):
        for y in range(*yrange):
            if color != board[x][y]:
                return None
    return color

def add_count(ca, cb):
    return (ca[0] + cb[0], ca[1] + cb[1])

def get_count(board, xrange, yrange):
    checked_color = check_range(board, xrange, yrange)
    if checked_color == 0:
        return (1, 0)
    elif checked_color == 1:
        return (0, 1)
    
    result = (0, 0)
    for new_xrange in divide_range(xrange):
        for new_yrange in divide_range(yrange):
            result = add_count(result, get_count(board, new_xrange, new_yrange))

    return result

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    board = [
        [1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1]
    ]

    equal(get_count(board, (0, 8), (0, 8)), (9, 7))

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    n = int(input())
    board = [None for _ in range(n)]
    for x in range(n):
        board[x] = input_list(int)
    c0, c1 = get_count(board, (0, n), (0, n))
    print(f"{c0}\n{c1}")

# Case-switch
if __name__ == '__main__':
    submit()