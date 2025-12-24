# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


# def backtrack(state):
#     if is_solution(state):
#         do_something(state)
#         return

#     for next_case in state:
#         state.add(next_case)
#         backtrack(state)
#         state.remove(next_case)


def main():
    """write your code here"""
    board = [None] * 9
    for i in range(9):
        board[i] = list(map(int, list(input_one(str))))

    def next_pos(pos):
        r, c = pos
        if r == 8 and c == 8:
            return "end"
        elif c == 8:
            return r + 1, 0
        return r, c + 1

    def print_board(board):
        for board_row in board:
            print("".join(map(str, board_row)))

    def possible_fills(pos):
        fills = [True] * 10
        fills[0] = False
        r, c = pos

        for dr in range(9):
            if dr != r:
                fills[board[dr][c]] = False

        for dc in range(9):
            if dc != c:
                fills[board[r][dc]] = False

        r_square = (r // 3) * 3
        c_square = (c // 3) * 3
        for dr in range(r_square, r_square + 3):
            for dc in range(c_square, c_square + 3):
                if r != dr or c != dc:
                    fills[board[dr][dc]] = False

        return [i for i in range(1, 10) if fills[i]]

    def backtrack(pos):
        if pos == "end":
            print_board(board)
            sys.exit(0)

        r, c = pos

        if board[r][c] != 0:
            backtrack(next_pos(pos))
        else:
            for fill in possible_fills(pos):
                board[r][c] = fill
                backtrack(next_pos(pos))
                board[r][c] = 0

    backtrack((0, 0))


main()
