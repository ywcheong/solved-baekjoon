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

MAX_POS = 100_001
INFINITE = float("inf")

def edge(v):
    connected = [
        (1, v-1),
        (1, v+1),
        (0, 2*v)
    ]

    return [w for w in connected if 0 <= w[1] < MAX_POS]

def solve_movement(start, target):
    to_visit, visited = [(0, start)], {start: 0}

    while to_visit:
        dist, v = heapq.heappop(to_visit)
        
        # 중복 탐색 방지:
        if dist > visited.get(v, INFINITE):
            continue
        assert dist == visited[v]

        # 탐색 시작
        for weight, w in edge(v):
            new_dist = dist + weight
            #  (미개척 노드거나)  or  (더 나은 개척로가 있거나)
            if w not in visited or new_dist < visited[w]:
                heapq.heappush(to_visit, (new_dist, w))
                visited[w] = new_dist

    return visited[target]


# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(solve_movement(5, 17), 2)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    start, target = input_list(int)
    print(solve_movement(start, target))

# Case-switch
if __name__ == '__main__':
    # test()
    submit()