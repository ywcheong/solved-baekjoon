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
sys.setrecursionlimit(10000)

def solve_lcs_length(s1, s2):
    # memo[p][q] := solve(s1[:p], s2[:q])
    memo = [[None] * (len(s2)+1) for _ in range(len(s1)+1)]
    
    # Initial Setup: solve('', str) == 0
    for p in range(len(s1)+1):
        memo[p][0] = 0
    for q in range(len(s2)+1):
        memo[0][q] = 0
    
    # Fillup (order: bottom-up)
    for p in range(1, len(s1)+1):
        for q in range(1, len(s2)+1):
            memo[p][q] = max(
                memo[p-1][q],
                memo[p][q-1],
                memo[p-1][q-1] + (s1[p-1] == s2[q-1]),
            )

    return memo[len(s1)][len(s2)]
            
# Recursion is slow... :(
# def get_lcs_with_index(s1, p, s2, q, memo):
#     # is equal to solve_lcs_length(s1[:p+1], s2[:q+1])

#     # Dead End: One is dead
#     if p < 0 or q < 0:
#         return 0
#     if memo[p][q] is not None:
#         return memo[p][q]
    
#     # LCS is one of
#     #   s1[:p], s2[:q-1]
#     #   s1[:p-1], s2[:q]
#     #   s1[:p-1], s2[:q-1] + I(s1[p] == s2[q])
#     result = get_lcs_with_index(s1, p-1, s2, q, memo)
#     result = max(result, get_lcs_with_index(s1, p, s2, q-1, memo))
#     result = max(result, get_lcs_with_index(s1, p-1, s2, q-1, memo) + (s1[p] == s2[q]))
#     memo[p][q] = result
#     return result


# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(solve_lcs_length('ACAYKP', 'CAPCAK'), 4)
    equal(solve_lcs_length('A'*1000, 'A'*1000), 1000)
    equal(solve_lcs_length('A'*1000, 'B'*1000), 0)
    equal(solve_lcs_length('AB'*500, 'BA'*500), 999)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    s1, s2 = input(), input()
    print(solve_lcs_length(s1, s2))

# Case-switch
if __name__ == '__main__':
    submit()