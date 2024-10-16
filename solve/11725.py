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
def get_adjacency(node, edge):
    result = dict()
    for v in node:
        result[v] = []
    for v, w in edge:
        result[v].append(w)
        result[w].append(v)
    return result

from collections import deque

def get_parent(node, edge):
    starting = [1]
    to_visit, visited = deque(starting), set(starting)
    parent = dict()

    while to_visit:
        v = to_visit.pop()
        for w in edge[v]:
            if w not in visited:
                to_visit.append(w)
                visited.add(w)
                parent[w] = v

    result = [None] * (len(node) - 1)
    for i in range(len(node)-1):
        result[i] = parent[i+2]

    return result

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    test_node_1 = [1,2,3,4,5,6,7]
    test_edge_1 = get_adjacency(test_node_1, [
        (1,6),
        (6,3),
        (3,5),
        (4,1),
        (2,4),
        (4,7)
    ])

    equal(get_parent(test_node_1, test_edge_1), [4,6,1,3,1,4])

    test_node_2 = [1,2,3,4,5,6,7,8,9,10,11,12]
    test_edge_2 = get_adjacency(test_node_2, [
        (1, 2),
        (1, 3),
        (2, 4),
        (3, 5),
        (3, 6),
        (4, 7),
        (4, 8),
        (5, 9),
        (5, 10),
        (6, 11),
        (6, 12)
    ])

    equal(get_parent(test_node_2, test_edge_2), [1,1,2,3,3,4,4,5,5,6,6])

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    N = int(input())
    node = list(range(1, N+1))
    edge = [None] * (N-1)
    for i in range(N-1):
        edge[i] = input_list(int)
    result = get_parent(node, get_adjacency(node, edge))
    print("\n".join(map(str, result)))
    

# Case-switch
if __name__ == '__main__':
    submit()