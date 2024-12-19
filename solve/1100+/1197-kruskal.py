# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def get_parent(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.get_parent(self.parent[n])
        return self.parent[n]

    def union_parent(self, n, m):
        n, m = self.get_parent(n), self.get_parent(m)
        if n != m:
            self.parent[n] = m


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    num_node, num_edge = input_list(int)
    edges = [None] * num_edge

    for i in range(num_edge):
        v1, w1, weight = input_list(int)
        edges[i] = (weight, v1 - 1, w1 - 1)

    edges.sort(key=lambda e: e[0])

    def mst_kruskal(num_node, edges):
        node_check = DisjointSet(num_node)
        mst = []
        mst_weight = 0

        for edge in edges:
            weight, v, w = edge

            if node_check.get_parent(v) != node_check.get_parent(w):
                mst.append(edge)
                mst_weight += weight
                node_check.union_parent(v, w)

            if len(mst) == num_node - 1:
                break

        return mst_weight

    print(mst_kruskal(num_node, edges))


main()
