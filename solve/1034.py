# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import Counter

def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))

def main():
    """write your code here"""
    nrow, ncolumn = input_list(int)
    board = [None] * nrow
    for i in range(nrow):
        board[i] = tuple(map(int, list(input_one(str))))
    npress = input_one(int)

    known_max = 0
    row_counts = Counter(board)

    for row in row_counts:
        column_count = Counter(row)
        if npress >= column_count[0] and (npress - column_count[0]) % 2 == 0:
            known_max = max(known_max, row_counts[row])
    
    print(known_max)

main()
