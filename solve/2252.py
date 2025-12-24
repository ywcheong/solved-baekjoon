# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def topology_sort(graph):
    '''Sort given DAG into List[Node]'''
    # compute indegree
    indegree = {v: 0 for v in graph}
    for v in graph:
        for w in graph[v]:
            indegree[w] += 1

    # prepare for Queue-traverse
    result, to_visit = list(), deque()
    for v in indegree:
        if indegree[v] == 0:
            to_visit.append(v)

    while to_visit:
        # remove v, and record
        v = to_visit.popleft()
        result.append(v)

        # For (v, w), check if w is insertable.
        for w in graph[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                to_visit.append(w)
    
    return result

def main():
    """write your code here"""
    num_node, num_edge = input_list(int)

    graph = {x: [] for x in range(1, num_node + 1)}

    for _ in range(num_edge):
        start, end = input_list(int)
        graph[start].append(end)

    return " ".join(map(str, topology_sort(graph)))


print(main())
