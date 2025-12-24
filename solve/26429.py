# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(num_node, edges, num_query):
    """write your logic here"""
    graph = {v: [] for v in range(1, num_node + 1)}
    for v, w in edges:
        graph[v].append(w)
        graph[w].append(v)
    level_count = {1: 1}
    to_visit, visited = deque([1]), {1: 1}

    while to_visit:
        v = to_visit.popleft()

        for w in graph[v]:
            if w not in visited:
                to_visit.append(w)
                visited[w] = visited[v] + 1
                level_count[visited[w]] = level_count.get(visited[w], 0) + 1
    
    # print(visited, level_count, num_query)

    count, level = 0, 1
    while level in level_count:
        if count + level_count[level] > num_query:
            break
        count += level_count[level]
        level += 1

    return count


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(solve(1, [], 1), 1)
    check(solve(3, [(1, 2), (1, 3)], 2), 1)
    check(solve(4, [(1, 2), (1, 3), (2, 4)], 4), 4)
    check(solve(5, [(1, 2), (1, 3), (5, 3), (2, 4)], 2), 1)


def main():
    """write your i/o here"""
    num_testcase = input_one(int)
    for testcase_id in range(1, num_testcase + 1):
        num_node, num_query = input_list(int)
        edges = [None] *(num_node - 1)
        for i in range(num_node - 1):
            edges[i] = input_list(int)

        query = [None] * num_query
        for j in range(num_query):
            query[j] = input_one(int)

        print(f"Case #{testcase_id}: {solve(num_node, edges, num_query)}")


# test()
main()
