# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def edmonds_karp(nodes, edges, source, sink):

    def bfs_from_source(residual):
        to_visit, visited = deque([source]), {source}
        parent = dict()
        
        while to_visit:
            v = to_visit.popleft()

            for w in nodes:
                if residual[v, w] > 0 and w not in visited:
                    to_visit.append(w)
                    visited.add(w)
                    parent[w] = v

                    if w == sink:
                        return parent
                    
        return None
    
    def get_flow(residual, parent):
        pos, flow = sink, float("inf")
        while pos != source:
            prev_pos = parent[pos]
            flow = min(flow, residual[prev_pos, pos])
            pos = prev_pos
        return flow
    
    def update_residual(residual, parent, flow):
        pos = sink
        while pos != source:
            prev_pos = parent[pos]
            residual[prev_pos, pos] -= flow
            residual[pos, prev_pos] += flow
            pos = prev_pos

    max_flow = 0
    residual = edges # same reference
    
    while parent := bfs_from_source(residual):
        # print(parent)
        flow = get_flow(residual, parent)
        # print(flow)
        max_flow += flow
        update_residual(residual, parent, flow)
        # print(residual)
    
    return max_flow


def main():
    """write your i/o here"""
    num_edge = input_one(int)
    
    nodes, edges = set(), dict()

    for _ in range(num_edge):
        v, w, capacity = input_list(str)
        capacity = int(capacity)

        if v == w:
            continue
        
        nodes.add(v)
        nodes.add(w)
        edges[v, w] = edges.get((v, w), 0) + capacity
        edges[w, v] = edges.get((w, v), 0) + capacity

    for v in nodes:
        for w in nodes:
            edges[v, w] = edges.get((v, w), 0)

    print(edmonds_karp(nodes, edges, 'A', 'Z'))

main()
