# My Solution : https://github.com/ywcheong/solved-baekjoon

# Header
''' import header here '''


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
''' write code here '''
def get_adjacent_matrix(node_count, edge):
    matrix = [[float("inf")]*(node_count) for _ in range(node_count)]
    for start, end, dist in edge:
        matrix[start-1][end-1] = min(dist, matrix[start-1][end-1])
    return matrix

def solve_shortest(node_count, edge):
    '''edge: edge[i][j] = (i -> j dist) or None'''
    edge = get_adjacent_matrix(node_count, edge)
    dist = [[None] * node_count for _ in range(node_count)]
    node_range = range(node_count)
    for start in node_range:
        for end in node_range:
            if start == end:
                dist[start][end] = 0
            elif edge[start][end] is not None:
                # initialize dist with edge
                dist[start][end] = edge[start][end]
    for mid in node_range:
        for start in node_range:
            for end in node_range:
                # update each dist for every possible mids
                dist[start][end] = min(dist[start][end], dist[start][mid] + dist[mid][end])
    for start in node_range:
        for end in node_range:
            if (this_dist := dist[start][end]) != float("inf"):
                dist[start][end] = this_dist
            else:
                dist[start][end] = 0
    return dist

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> OK (1 == 1)
    # equal(2, 1) -> FAIL (2 == 1)
    equal(solve_shortest(5, [
        (1, 2, 2),
        (1, 3, 3),
        (1, 4, 1),
        (1, 5, 10),
        (2, 4, 2),
        (3, 4, 1),
        (3, 5, 1),
        (4, 5, 3),
        (3, 5, 10),
        (3, 1, 8),
        (1, 4, 2),
        (5, 1, 7),
        (3, 4, 2),
        (5, 2, 4),
    ]), [
        [0, 2, 3, 1, 4],
        [12, 0, 15, 2, 5],
        [8, 5, 0, 1, 1],
        [10, 7, 13, 0, 3],
        [7, 4, 10, 6, 0],
    ])

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    node_count = int(input())
    edge_count = int(input())
    edge = [None] * edge_count

    for i in range(edge_count):
        edge[i] = input_list(int)

    result = solve_shortest(node_count, edge)
    for row in result:
        print(" ".join(map(str, row)))

# Case-switch
if __name__ == '__main__':
    # test()
    submit()