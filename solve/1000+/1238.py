# My Solution : https://github.com/ywcheong/solved-baekjoon

# Header
""" import header here """


import sys

input = lambda: sys.stdin.readline().strip()
input_list = lambda wanted_type: list(map(wanted_type, input().split()))

TESTCASE_ID = 1


def equal(left, right):
    global TESTCASE_ID
    if left == right:
        print(f"Testcase {TESTCASE_ID}: OK ({left} == {right})")
    else:
        print(f"Testcase {TESTCASE_ID}: FAIL ({left} != {right})")
    TESTCASE_ID += 1


# Implementation
""" write code here """
import heapq

def get_adjacency_map(node_count, edges):
    edge_forward, edge_backward = dict(), dict()
    for start, end, dist in edges:
        edge_forward[start] = edge_forward.get(start, []) + [(dist, end)]
        edge_backward[end] = edge_backward.get(end, []) + [(dist, start)]
    return edge_forward, edge_backward


def get_shortest(node_count, edges, starting):
    to_visit, visited = [(0, starting)], {starting: 0}

    while to_visit:
        dist, v = heapq.heappop(to_visit)

        # 만료된 노드 삭제
        if dist > visited[v]:
            continue

        for weight, w in edges[v]:
            new_dist = dist + weight
            # 탐색된 적 없거나 or 더 짧은 거리 발견
            if w not in visited or new_dist < visited[w]:
                heapq.heappush(to_visit, (new_dist, w))
                visited[w] = new_dist

    return visited


def solve_longest(node_count, edges, town_center):
    edge_forward, edge_backward = get_adjacency_map(node_count, edges)
    home_to_center_time = get_shortest(node_count, edge_backward, town_center)
    center_to_home_time = get_shortest(node_count, edge_forward, town_center)
    
    result = 0
    for home in range(1, node_count+1):
        result = max(result, home_to_center_time[home] + center_to_home_time[home])
    return result


# Testing
def test():
    print("WARNING: TEST MODE")

    """ test here """
    # equal(1, 1) -> OK (1 == 1)
    # equal(2, 1) -> FAIL (2 == 1)

    print("TEST DONE")


# Submit
def submit():
    """get input here"""
    node_count, edge_count, town_center = input_list(int)
    edges = [None] * edge_count
    for i in range(edge_count):
        edges[i] = input_list(int)
    print(solve_longest(node_count, edges, town_center))


# Case-switch
if __name__ == "__main__":
    # test()
    submit()
