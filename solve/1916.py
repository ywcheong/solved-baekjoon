# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
import heapq


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    node_count, edge_count = input_one(int), input_one(int)

    edge = [list() for _ in range(node_count + 1)]
    for _ in range(edge_count):
        v, w, weight = input_list(int)
        edge[v].append((weight, w))

    start, target = input_list(int)
    to_visit = [(0, start)]
    visited = [float("inf")] * (node_count + 1)

    while to_visit:
        dist, v = heapq.heappop(to_visit)

        # 만료된 노드 제거
        if dist > visited[v]:
            continue

        if v == target:
            print(dist)
            return

        for weight, w in edge[v]:
            # 더 나은 개척로 발견
            if (new_dist := dist + weight) < visited[w]:
                visited[w] = new_dist
                heapq.heappush(to_visit, (new_dist, w))

    raise AssertionError("Cannot reach here")


main()
