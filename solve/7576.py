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
from collections import deque

def edge(board, v):
    N, M = len(board), len(board[0])
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    i, j = v

    result = []
    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 0:
            result.append((ni, nj))
    return result


def get_day(board):
    N, M = len(board), len(board[0])
    to_visit, visited, layer = deque(), set(), dict()

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                pos = (i, j)
                to_visit.append(pos)
                visited.add(pos)
                layer[pos] = 0

    while to_visit:
        v = to_visit.popleft()
        for w in edge(board, v):
            if w not in visited:
                to_visit.append(w)
                visited.add(w)
                layer[w] = layer[v] + 1

    # return layer

    result = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != -1 and (i, j) not in layer:
                return -1
            elif board[i][j] != -1:
                result = max(result, layer[(i, j)])

    return result
    

def convert_input(lines):
    result = [None] * len(lines)
    for i in range(len(result)):
        result[i] = list(map(int, lines[i].split()))
    return result

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    test_1 = """0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1""".split("\n")

    test_2 = """0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1""".split("\n")
    
    test_3 = """1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1""".split("\n")
    
    test_4 = """-1 1 0 0 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 0 0 0 0""".split("\n")
    
    test_5 = """1 -1
-1 1""".split("\n")

    equal(get_day(convert_input(test_1)), 8)
    equal(get_day(convert_input(test_2)), -1)
    equal(get_day(convert_input(test_3)), 6)
    equal(get_day(convert_input(test_4)), 14)
    equal(get_day(convert_input(test_5)), 0)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    M, N = input_list(int)
    lines = [None] * N
    for i in range(N):
        lines[i] = input()

    print(get_day(convert_input(lines)))

# Case-switch
if __name__ == '__main__':
    submit()