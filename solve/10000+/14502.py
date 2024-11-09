# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


CELL_EMPTY = 0
CELL_WALL = 1
CELL_VIRUS = 2


def main():
    """write your code here"""
    row, column = input_list(int)
    given_board = [None] * row

    empty_list, virus_list = [], []

    for i in range(row):
        given_board[i] = input_list(int)
        for j in range(column):
            if given_board[i][j] == CELL_EMPTY:
                empty_list.append((i, j))
            elif given_board[i][j] == CELL_VIRUS:
                virus_list.append((i, j))

    total_size = row * column
    wall_size = total_size - len(empty_list) - len(virus_list)

    def compute_nextpos(board, pos):
        """Given virus pos, compute next infectable adjacent List[pos]."""
        x, y = pos
        result = []
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < row and 0 <= ny < column and board[nx][ny] == CELL_EMPTY:
                result.append((nx, ny))
        return result

    def compute_safearea(board, virus_list):
        """Given board and init virus List[pos], compute non-infected area size."""
        to_visit = virus_list[:]
        visited = set(pos for pos in virus_list)

        while to_visit:
            v = to_visit.pop()

            for w in compute_nextpos(board, v):
                if w not in visited:
                    to_visit.append(w)
                    visited.add(w)

        # (Safe size) = (Total size) - (Wall size) - (Infected size)
        return total_size - (wall_size + 3) - len(visited)

    known_max = 0

    for i in range(len(empty_list)):
        for j in range(i + 1, len(empty_list)):
            for k in range(j + 1, len(empty_list)):
                # Pick three empty place, then make walls...
                for x, y in (empty_list[i], empty_list[j], empty_list[k]):
                    given_board[x][y] = CELL_WALL

                # and get safe amount...
                known_max = max(known_max, compute_safearea(given_board, virus_list))

                # and remove walls, and repeat...
                for x, y in (empty_list[i], empty_list[j], empty_list[k]):
                    given_board[x][y] = CELL_EMPTY

    return known_max


print(main())
