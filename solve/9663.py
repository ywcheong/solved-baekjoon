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
def solve_queen(n):
    result = 0

    def is_valid(queens, level, column):
        '''Check if it is good to place new queen at `(x, y)`'''
        for old_level, old_column in enumerate(queens[:level]):
            if column == old_column or (level - old_level) == abs(column - old_column):
                return False
        return True

    # queens[i] = j <-> queen at (i, j)
    def backtrack(queens, level):
        '''Backtracking Algorithm for `solve_queen`'''
        # Good End: All Queens Placed
        if level == n:
            nonlocal result
            result += 1
            return
        
        # Forward-Search-Backward
        for column in range(n):
            if is_valid(queens, level, column):
                queens[level] = column           # Forward  : Place Queen
                backtrack(queens, level+1)       # Search   : Further Backtracking
    
    backtrack([None]*n, 0)
    return result

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(solve_queen(1), 1)
    equal(solve_queen(2), 0)
    equal(solve_queen(3), 0)
    equal(solve_queen(4), 2)
    equal(solve_queen(8), 92)
    print(solve_queen(14))
    
    import cProfile
    # cProfile.run('solve_queen(12)')

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    n = int(input())
    print(solve_queen(n))

# Case-switch
if __name__ == '__main__':
    submit()