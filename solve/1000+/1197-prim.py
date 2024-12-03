# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
import heapq


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def mst_prim(nodes, edges):
    starting = next(iter(nodes))
    to_visit, mst = [(0, starting)], set()
    cost = 0

    while to_visit:
        dist, v = heapq.heappop(to_visit)

        if v in mst:
            continue

        cost += dist
        mst.add(v)
        
        for weight, w in edges[v]:
            if w not in mst:
                heapq.heappush(to_visit, (weight, w))

    return cost

def main():
    """write your code here"""
    num_node, num_edge = input_list(int)

    nodes = range(1, num_node + 1)
    edges = dict()

    for v in nodes:
        edges[v] = []

    for _ in range(num_edge):
        v, w, weight = input_list(int)
        edges[v].append((weight, w))
        edges[w].append((weight, v))

    print(mst_prim(range(1, num_node + 1), edges))


main()
