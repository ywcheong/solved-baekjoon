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
def ascii_to_int(ascii):
    if ascii == '.':
        return None
    return ord(ascii) - 65

def traverse_NLR(nodes, index):
    if index is None:
        return ''
    
    this, left_index, right_index = nodes[index]
    return this + traverse_NLR(nodes, left_index) + traverse_NLR(nodes, right_index)

def traverse_LNR(nodes, index):
    if index is None:
        return ''
    
    this, left_index, right_index = nodes[index]
    return traverse_LNR(nodes, left_index) + this + traverse_LNR(nodes, right_index)

def traverse_LRN(nodes, index):
    if index is None:
        return ''
    
    this, left_index, right_index = nodes[index]
    return traverse_LRN(nodes, left_index) + traverse_LRN(nodes, right_index) + this

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    N = int(input())
    nodes = [None] * N
    for _ in range(N):
        this, left, right = input_list(str)
        nodes[ascii_to_int(this)] = (this, ascii_to_int(left), ascii_to_int(right))

    print(traverse_NLR(nodes, 0))
    print(traverse_LNR(nodes, 0))
    print(traverse_LRN(nodes, 0))

# Case-switch
if __name__ == '__main__':
    submit()