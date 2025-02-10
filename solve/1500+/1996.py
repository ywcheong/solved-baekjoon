# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys

PINF = float("inf")


def solve(board):
    """write your solution here"""

    size = len(board)
    result = [
        [0 if board[x][y] == 0 else PINF for y in range(size)] for x in range(size)
    ]

    for x in range(size):
        for y in range(size):
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < size and 0 <= ny < size:
                        result[nx][ny] += board[x][y]

    return result


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""


def mask(num_mine):
    if num_mine == PINF:
        return "*"

    if num_mine >= 10:
        return "M"

    return num_mine


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    size = input_one(int)
    board = [None] * size
    for x in range(size):
        board[x] = [0 if char == "." else int(char) for char in input_one(str)]

    result = solve(board)
    for row in result:
        for char in row:
            print(mask(char), end="")
        print()


# test()
main()
