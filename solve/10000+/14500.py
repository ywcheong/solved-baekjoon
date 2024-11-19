# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))

block_list = [
    (
        (1, 1, 1, 1,),
    ),
    (
        (1,),        
        (1,),        
        (1,),        
        (1,),        
    ),
    (
        (1, 1,),
        (1, 1,),
    ),
    (
        (1, 1,),
        (1, 0,),
        (1, 0,),
    ),
    (
        (1, 0,),
        (1, 0,),
        (1, 1,),
    ),
    (
        (1, 1,),
        (0, 1,),
        (0, 1,),
    ),
    (
        (0, 1,),
        (0, 1,),
        (1, 1,),
    ),
    (
        (1, 1, 1,),
        (1, 0, 0,),
    ),
    (
        (1, 1, 1,),
        (0, 0, 1,),
    ),
    (
        (1, 0, 0,),
        (1, 1, 1,),
    ),
    (
        (0, 0, 1,),
        (1, 1, 1,),
    ),
    (
        (1, 0,),
        (1, 1,),
        (0, 1,),
    ),
    (
        (0, 1,),
        (1, 1,),
        (1, 0,),
    ),
    (
        (0, 1, 1,),
        (1, 1, 0,),
    ),
    (
        (1, 1, 0,),
        (0, 1, 1,),
    ),
    (
        (0, 1,),
        (1, 1,),
        (0, 1,),
    ),
    (
        (1, 0,),
        (1, 1,),
        (1, 0,),
    ),
    (
        (0, 1, 0,),
        (1, 1, 1,),
    ),
    (
        (1, 1, 1,),
        (0, 1, 0,),
    ),
]

def main():
    """write your code here"""
    row, column = input_list(int)
    board = [None] * row

    for i in range(row):
        board[i] = input_list(int)

    known_max = 0

    for block in block_list:
        height, width = len(block), len(block[0])
        for i in range(row-height+1):
            for j in range(column-width+1):
                current_sum = 0
                for di in range(height):
                    for dj in range(width):
                        current_sum += board[i+di][j+dj] * block[di][dj]
                known_max = max(known_max, current_sum)

    return known_max

print(main())
