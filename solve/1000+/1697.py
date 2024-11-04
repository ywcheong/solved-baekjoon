# My Solution : https://github.com/ywcheong/solved-baekjoon

# Header
''' import header here '''
from collections import deque

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
def edge(v):
    return [x for x in (v-1, v+1, 2*v) if 0 <= x <= 100000]

def get_time(start, target):
    if start == target:
        return 0
    
    to_visit, visited = deque([start]), set([start])
    depth = {start: 0}

    while to_visit:
        v = to_visit.popleft()

        for w in edge(v):
            if w not in visited:
                to_visit.append(w)
                visited.add(w)
                depth[w] = depth[v] + 1

                if w == target:
                    return depth[target]
                
    # It must terminate before here
    raise Exception("uh")

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    equal(get_time(5, 17), 4)
    equal(get_time(5, 5), 0)
    equal(get_time(5, 4), 1)
    equal(get_time(5, 6), 1)
    equal(get_time(5, 10), 1)
    equal(get_time(100000, 0), 100000)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    start, target = input_list(int)
    print(get_time(start, target))

# Case-switch
if __name__ == '__main__':
    submit()