# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input().split()))


BEFORE_PASS, AFTER_PASS = 0, 1

def main():
    """write your code here"""
    n, m = input_list(int)
    board = [None] * n
    for i in range(n):
        board[i] = list(map(int, input_one(str)))

    if n == m == 1:
        print(1)
        return
    
    distance = [[[None for _ in range(m)] for __ in range(n)] for ___ in range(2)]
    distance[BEFORE_PASS][0][0] = 1
    to_visit = deque([])
    to_visit.append((BEFORE_PASS, 0, 0))

    def get_next(pos):
        this_pass, i, j = pos
        result = []

        for next_i, next_j in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if not (0 <= next_i < n and 0 <= next_j < m):
                continue

            if board[next_i][next_j] == 0:
                result.append((this_pass, next_i, next_j))
            elif this_pass == BEFORE_PASS:
                result.append((AFTER_PASS, next_i, next_j))

        return result


    while to_visit:
        pos = to_visit.popleft()
        current_distance = distance[pos[0]][pos[1]][pos[2]]

        for next_pos in get_next(pos):
            next_pass, next_i, next_j = next_pos
            if distance[next_pass][next_i][next_j] is None:
                to_visit.append(next_pos)
                distance[next_pass][next_i][next_j] = current_distance + 1
                if next_i == n-1 and next_j == m-1:
                    print(current_distance + 1)
                    return
    
    print(-1)
    return


main()
