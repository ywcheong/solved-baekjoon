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
def get_adjacency(node, edge):
    result = dict()

    for x in node:
        result[x] = []
    
    for v, w in edge:
        result[v].append(w)
        result[w].append(v)

    return result

def get_component(node, edge):
    unvisited = set(node)
    result = 0
    while len(unvisited) > 0:
        starting = [unvisited.pop()]
        result += 1
        to_visit, visited = deque(starting), set(starting)

        while len(to_visit) > 0:
            v = to_visit.pop()
            for w in edge[v]:
                if w not in visited:
                    unvisited -= {w}
                    visited |= {w}
                    to_visit.append(w)
        
    return result

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    node1 = list(range(1, 7))
    edge1 = get_adjacency(node1, [(1, 2), (2, 5), (5, 1), (3, 4), (4, 6)])

    equal(get_component(node1, edge1), 2)

    node2 = list(range(1, 7))
    edge2 = get_adjacency(node2, [(1, 2), (2, 5), (5, 1), (3, 4), (4, 6), (5, 4), (2, 4), (2, 3)])

    equal(get_component(node2, edge2), 1)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    V, E = input_list(int)
    node = list(range(1, V+1))
    edge = []

    for _ in range(E):
        v, w = input_list(int)
        edge.append((v, w))
    
    edge = get_adjacency(node, edge)
    print(get_component(node, edge))

# Case-switch
if __name__ == '__main__':
    submit()