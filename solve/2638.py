# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


INNER_AIR_BLOCK, CHEESE_BLOCK, OUTER_AIR_BLOCK = 0, 1, 2


def is_cheese_exist(board):
    return any(cell == CHEESE_BLOCK  for row in board for cell in row)


def get_starting(board):
    num_row, num_column = len(board), len(board[0])
    result = []
    result += [(0, c) for c in range(num_column)]
    result += [(num_row - 1, c) for c in range(num_column)]
    result += [(r, 0) for r in range(1, num_row - 1)]
    result += [(r, num_column - 1) for r in range(1, num_row - 1)]
    return result


def make_exposed(board):
    starting = get_starting(board)
    to_visit, visited = starting, set(starting)
    exposed = []

    while to_visit:
        v = to_visit.pop()
        r, c = v

        if board[r][c] == CHEESE_BLOCK:
            exposed.append(v)
            continue
        else:
            board[r][c] = OUTER_AIR_BLOCK

        for w in get_adjacent(board, v):
            if w not in visited:
                to_visit.append(w)
                visited.add(w)

    return exposed


def get_adjacent(board, pos):
    num_row, num_column = len(board), len(board[0])
    r, c = pos

    result = []
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if 0 <= nr < num_row and 0 <= nc < num_column:
            result.append((nr, nc))

    return result


def get_adjacent_air_num(board, exposed_pos):
    adjacent_list = get_adjacent(board, exposed_pos)
    count = 0
    for r, c in adjacent_list:
        if board[r][c] == OUTER_AIR_BLOCK:
            count += 1
    return count


def main():
    """write your code here"""
    num_row, num_column = input_list(int)
    board = [None] * (num_row + 2)
    board[0] = [OUTER_AIR_BLOCK] * (num_column + 2)
    board[-1] = [OUTER_AIR_BLOCK] * (num_column + 2)

    for i in range(num_row):
        board[1 + i] = [OUTER_AIR_BLOCK] + input_list(int) + [OUTER_AIR_BLOCK]

    iter = 0

    while is_cheese_exist(board):
        # print(f"======== [iter = {iter}] ========")
        # for row in board:
        #     print(" ".join(map(str, row)))
        iter += 1
        exposed_list = make_exposed(board)
        melt_list = []

        for exposed in exposed_list:
            if get_adjacent_air_num(board, exposed) >= 2:
                melt_list.append(exposed)
        
        for r, c in melt_list:
            board[r][c] = OUTER_AIR_BLOCK

    print(iter)
    return iter


main()

