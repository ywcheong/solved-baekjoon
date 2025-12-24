# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque

sys.setrecursionlimit(1_100_000)


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


PINF = 987_654_321


def solve(num_node, graph):
    """write your logic here"""
    if num_node == 1:
        return 1
    elif num_node == 2:
        return 1

    def is_leaf(node):
        return len(graph[node]) == 1

    starting = 1
    while is_leaf(starting):
        starting += 1

    def _recursion(prev_node, this_node):
        if is_leaf(this_node):
            raise ValueError("Cannot perform recursion over leaf node")

        child_costs = []
        for next_node in graph[this_node]:
            if next_node == prev_node:
                continue

            if is_leaf(next_node):
                child_costs.append((0, 1))
            else:
                child_costs.append(_recursion(this_node, next_node))

        # Case 2: this_node가 얼리어답터 아님: Black만 선택
        white_cost = sum([bc for wc, bc in child_costs])

        # Case 1: this_node가 얼리어답터: 둘 중 싼 걸로 선택
        black_cost = sum([min(wc, bc) for wc, bc in child_costs]) + 1

        # print(f"Node[[{prev_node}->{this_node}]: Wc[{white_cost}] Bc[{black_cost}] Childs[{child_costs}]")

        return white_cost, black_cost

    return min(_recursion(None, starting))


def main():
    """write your i/o here"""
    num_node = input_one(int)
    graph = dict()

    for _ in range(num_node - 1):
        v, w = input_list(int)
        graph[v] = graph.get(v, []) + [w]
        graph[w] = graph.get(w, []) + [v]

    print(solve(num_node, graph))


main()
