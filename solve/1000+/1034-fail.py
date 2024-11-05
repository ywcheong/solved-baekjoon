# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))

def main():
    """write your code here"""
    nrow, ncolumn = input_list(int)
    board = [None] * nrow
    for i in range(nrow):
        board[i] = list(map(int, list(input_one(str))))
    npress = input_one(int)

    known_max = 0

    def is_available(row, col, is_press):
        return (board[row][col] and not is_press) or (not board[row][col] and is_press)

    def backtrack(possible_rows: set, col, remain_press):
        nonlocal known_max

        if col == ncolumn:
            if remain_press % 2 == 0:
                known_max = max(known_max, len(possible_rows))
            return
        
        for is_press in (True, False):
            if is_press and remain_press == 0:
                continue
            
            opt_out = set()
            for row in range(nrow):
                if not is_available(row, col, is_press) and row in possible_rows:
                    opt_out.add(row)
                    possible_rows.remove(row)

            if len(possible_rows) > known_max:
                if is_press:
                    backtrack(possible_rows, col + 1, remain_press - 1)
                else:
                    backtrack(possible_rows, col + 1, remain_press)

            for row in opt_out:
                possible_rows.add(row)

    backtrack(set(range(nrow)), 0, npress)
    print(known_max)


main()
