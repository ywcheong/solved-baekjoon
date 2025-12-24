# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


PINF = float("inf")


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(times, graph):
    """write your logic here"""
    num_build = len(times)
    parent_count = [0] * num_build

    for v in range(num_build):
        for w in graph[v]:
            parent_count[w] += 1

    to_visit, visited = [], [0] * num_build
    for v in range(num_build):
        if parent_count[v] == 0:
            to_visit.append(v)
            visited[v] = times[v]

    while to_visit:
        v = to_visit.pop()
        # print(f"Node[{v}] tovisit[{to_visit}] visited[{visited}] PC[{parent_count}]")

        for w in graph[v]:
            parent_count[w] -= 1
            visited[w] = max(visited[w], times[w] + visited[v])
            if parent_count[w] == 0:
                to_visit.append(w)

    return visited


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    check(solve([10, 10, 4, 4, 3], [[1, 2, 3], [], [3, 4], [], []]), [10, 20, 14, 18, 17])


def main():
    """write your i/o here"""
    num_build = input_one(int)
    times = [None for _ in range(num_build)]
    graph = [[] for _ in range(num_build)]

    for w in range(num_build):
        line = input_list(int)
        graph_len = len(line) - 2
        times[w] = line[0]
        for i in range(graph_len):
            graph[line[i + 1] - 1].append(w)

    print("\n".join(map(str, solve(times, graph))))


# test()
main()
