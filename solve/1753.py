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
import heapq

INFINITY = float("inf")

def get_adjacent_edge(edge):
    adj_edge = dict()
    for v, w, weight in edge:
        if v not in adj_edge:
            adj_edge[v] = [(weight, w)]
        else:
            adj_edge[v].append((weight, w))
    return adj_edge

def solve_shortest(node, adj_edge, start):
    # print(node, adj_edge, start)
    to_visit, visited = [(0, start)], {start: 0}
    
    while to_visit:
        dist, v = heapq.heappop(to_visit)

        # 만료 노드 제거
        if dist > visited.get(v, INFINITY):
            continue

        for weight, w in adj_edge.get(v, []):
            new_dist = dist + weight
            if w not in visited or new_dist < visited[w]:
                heapq.heappush(to_visit, (new_dist, w))
                visited[w] = new_dist

    return [str(visited.get(n, 'INF')) for n in range(1, node+1)]

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    equal(solve_shortest(5, get_adjacent_edge([
        (5, 1, 1),
        (1, 2, 2),
        (1, 3, 3),
        (2, 3, 4),
        (2, 4, 5),
        (3, 4, 6),
    ]), 1), ['0', '2', '3', '7', 'INF'])

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    node_count, edge_count = input_list(int)
    start = int(input())
    edge = [None] * edge_count
    for i in range(edge_count):
        edge[i] = input_list(int)

    result = solve_shortest(node_count, get_adjacent_edge(edge), start)
    print("\n".join(result))

# Case-switch
if __name__ == '__main__':
    # test()
    submit()