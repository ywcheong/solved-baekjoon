"""
    NOTICE : THIS IS CHATGPT-CONVERTED CODE OF 1916.py
            THIS IS NOT MY OWN WORK BUT AI'S
"""

import sys
import heapq


def input_one(given_type):
    return given_type(sys.stdin.readline())


def input_list(given_type):
    return list(map(given_type, sys.stdin.readline().split()))

def main():
    node_count = input_one(int)
    edge_count = input_one(int)

    edges = [[] for _ in range(node_count + 1)]
    for _ in range(edge_count):
        u, v, w = input_list(int)
        edges[u].append((w, v))

    start, end = input_list(int)

    visited = [float("inf")] * (node_count + 1)
    visited[start] = 0
    to_visit = [(0, start)]

    while to_visit:
        dist, v = heapq.heappop(to_visit)

        if v == end:
            print(dist)
            return

        if dist > visited[v]:
            continue

        for weight, w in edges[v]:
            new_dist = dist + weight
            if new_dist < visited[w]:
                visited[w] = new_dist
                heapq.heappush(to_visit, (new_dist, w))

    return -1  # If end is not reachable

main()
