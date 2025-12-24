# My Solution : https://github.com/ywcheong/solved-baekjoon

# Header
''' import header here '''
from collections import deque, defaultdict

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
def edge(board, pos):
    N, M = len(board), len(board[0])
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    x, y = pos

    return [(x+dx, y+dy) for dx, dy in delta if 0 <= x + dx < N and 0 <= y + dy < M and board[x+dx][y+dy] == 1]


def get_dist(board, starting):
    N, M = len(board), len(board[0])
    to_visit, visited = deque([starting]), set([starting])
    result = [[(0 if board[i][j] == 0 else -1) for j in range(M)] for i in range(N)]
    result[starting[0]][starting[1]] = 0

    while to_visit:
        v = to_visit.popleft()
        for w in edge(board, v):
            if w not in visited:
                to_visit.append(w)
                visited.add(w)
                result[w[0]][w[1]] = result[v[0]][v[1]] + 1

    return result


# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    test_starting, test_board = (0, 0), [
        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
    ]

    test_result = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
        [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
        [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
        [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 0, 0, 0, 25],
        [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0, 29, 28, 27, 26],
        [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 0, 30, 0, 0, 0],
        [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 31, 32, 33, 34]
    ]

    equal(get_dist(test_board, test_starting), test_result)

    equal(get_dist([
        [1, 1, 1],
        [1, 2, 1],
        [0, 0, 1],
        [1, 0, 1]
    ], (1, 1)), [
        [2, 1, 2],
        [1, 0, 1],
        [0, 0, 2],
        [-1, 0, 3]
    ])

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    N, M = input_list(int)
    starting = None
    board = [None] * N

    for i in range(N):
        board[i] = input_list(int)
        if 2 in board[i]:
            starting = (i, board[i].index(2))

    result = get_dist(board, starting)
    for row in result:
        print(" ".join(map(str, row)))

# Case-switch
if __name__ == '__main__':
    submit()