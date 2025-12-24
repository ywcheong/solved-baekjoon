# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def compute_ref_count(node_count, edge):
    ref_count = {x: 0 for x in range(1, node_count + 1)}

    for v in edge:
        for w in edge[v]:
            ref_count[w] += 1
    
    return ref_count


def main():
    """write your code here"""
    node_count, rule_count = input_list(int)
    edge = {x : set() for x in range(1, node_count + 1)}

    for _ in range(rule_count):
        rule = input_list(int)
        for start, end in zip(rule[1:-1], rule[2:]):
            edge[start].add(end)
    
    ref_count = compute_ref_count(node_count, edge)
    to_visit, visited = deque(), list()
    for v in edge:
        if ref_count[v] == 0:
            to_visit.append(v)
            visited.append(v)

    while to_visit:
        v = to_visit.popleft()

        for w in edge[v]:
            ref_count[w] -= 1
            if ref_count[w] == 0:
                to_visit.append(w)
                visited.append(w)

    if len(visited) == node_count:
        print("\n".join(map(str, visited)))
    else:
        print(0)

main()
