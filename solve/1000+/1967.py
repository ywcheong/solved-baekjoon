#############################################
#     THIS SOLUTION IS BASED ON 1967.py     #
#############################################

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
from collections import deque, defaultdict

def get_adjacent_map(edge):
    adjacent_map = defaultdict(list)
    for start, end, weight in edge:
        adjacent_map[start].append((weight, end))
        adjacent_map[end].append((weight, start))
    return adjacent_map

def get_farthest(edge, starting):
    to_visit, visited = deque([starting]), {starting: 0}
    max_dist, max_node = 0, starting

    while to_visit:
        v = to_visit.popleft()
        for dist, w in edge[v]:
            if w not in visited:
                to_visit.append(w)
                visited[w] = visited[v] + dist
                if visited[w] > max_dist:
                    max_dist, max_node = visited[w], w

    return max_dist, max_node

def solve_diameter(edge):
    adjacent_map = get_adjacent_map(edge)

    _, v = get_farthest(adjacent_map, 1)
    result, _ = get_farthest(adjacent_map, v)

    return result

# Testing
def test():
    print("WARNING: TEST MODE")

    """ test here """
    # equal(1, 1) -> OK (1 == 1)
    # equal(2, 1) -> FAIL (2 == 1)
    equal(
        solve_diameter(
            [
                (1, 2, 3),
                (1, 3, 2),
                (2, 4, 5),
                (3, 5, 11),
                (3, 6, 9),
                (4, 7, 1),
                (4, 8, 7),
                (5, 9, 15),
                (5, 10, 4),
                (6, 11, 6),
                (6, 12, 10),
            ]
        ),
        45,
    )

    equal(
        solve_diameter(
            [
                (1, 2, 3),
                (1, 3, 2),
                (3, 4, 7),
                (3, 5, 11),
            ]
        ),
        18,
    )

    equal(
        solve_diameter(
            [
                (1, 2, 20),
                (1, 3, 2),
                (3, 4, 7),
                (3, 5, 11),
            ]
        ),
        33
    )

    import cProfile
    cProfile.run('solve_diameter([(v, v+1, v**2) for v in range(1, 99_999)])')

    print("TEST DONE")


# Submit
def submit():
    """get input here"""
    node_count = int(input())
    edge = []
    for _ in range(node_count):
        line = input_list(int)
        start = line[0]
        end_list, weight_list = line[1:-1:2], line[2:-1:2]
        for end, weight in zip(end_list, weight_list):
            if end < start:
                continue
            edge.append((start, end, weight))
    print(solve_diameter(edge))

# Case-switch
if __name__ == "__main__":
    # test()
    submit()