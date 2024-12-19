# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(board):
    """write your logic here"""
    for row in range(10):
        if all(board[row][j] == board[row][0] for j in range(10)):
            return 1

    for column in range(10):
        if all(board[i][column] == board[0][column] for i in range(10)):
            return 1

    return 0


def test():
    """write your test here"""
    assert 1 == 1


def main():
    """write your i/o here"""
    board = [None] * 10

    for i in range(10):
        board[i] = input_list(str)
        assert len(board[i]) == 10

    print(solve(board))


test()
main()
