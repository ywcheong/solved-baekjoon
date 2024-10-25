# My Solution : https://github.com/ywcheong/solved-baekjoon

# Header
''' import header here '''


import sys
input_one = lambda wanted_type: wanted_type(sys.stdin.readline().strip())
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
def solve_negative_cycle(node_count, edge):
    dist = [987_654_321] * (node_count + 1)
    dist[1] = 0

    for step in range(1, node_count + 1):
        for start, end, weight in edge:
            if dist[end] > (new_dist := dist[start] + weight):
                dist[end] = new_dist
                if step == node_count:
                    return "YES"
                
    return "NO"

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> OK (1 == 1)
    # equal(2, 1) -> FAIL (2 == 1)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    testcase_count = input_one(int)
    for _ in range(testcase_count):
        node_count, road_count, warp_count = input_list(int)
        edge = []
        for i in range(road_count):
            start, end, weight = input_list(int)
            edge.append((start, end, weight))
            edge.append((end, start, weight))
        for i in range(warp_count):
            start, end, weight = input_list(int)
            edge.append((start, end, -weight))
        print(solve_negative_cycle(node_count, edge))

# Case-switch
if __name__ == '__main__':
    #test()
    submit()