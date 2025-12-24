# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


CELL_EMPTY, CELL_WALL, CELL_DOC = 0, 1, 2

SMALL_A_START, BIG_A_START = ord("a"), ord("A")


def key_to_open_door(key):
    return key - 32


def is_key_cell(cell):
    return 97 <= cell <= 122


def is_door_cell(cell):
    return 65 <= cell <= 90


def parse_board_row(input_line, open_doors):
    row = [CELL_EMPTY]
    for c in input_line:
        if c == "." or c in open_doors:
            row.append(CELL_EMPTY)
        elif c == "*":
            row.append(CELL_WALL)
        elif c == "$":
            row.append(CELL_DOC)
        else:
            row.append(ord(c))

    row.append(CELL_EMPTY)
    return row


def get_surroundings(board):
    row, column = len(board), len(board[0])

    open_entries = set()
    open_entries |= {(0, c) for c in range(column) if board[0][c] != CELL_WALL}
    open_entries |= {(r, 0) for r in range(1, row - 1) if board[r][0] != CELL_WALL}
    open_entries |= {
        (r, column - 1) for r in range(1, row - 1) if board[r][column - 1] != CELL_WALL
    }
    open_entries |= {
        (row - 1, c) for c in range(column) if board[row - 1][c] != CELL_WALL
    }

    return open_entries


def get_adjacent(board, pos):
    row, column = len(board), len(board[0])
    i, j = pos

    result = []
    for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if 0 <= ni < row and 0 <= nj < column and board[ni][nj] != CELL_WALL:
            result.append((ni, nj))
    return result


def main():
    """write your code here"""
    num_test = input_one(int)

    document_count = []

    for _ in range(num_test):
        document_count.append(0)
        row, column = input_list(int)

        board = [None] * (row + 2)
        board[0] = [CELL_EMPTY] * (column + 2)
        board[-1] = [CELL_EMPTY] * (column + 2)

        for i in range(row):
            board[i + 1] = input_one(str)

        key_list = input_one(str)
        open_doors = set()
        if key_list != "0":
            for key in key_list:
                open_doors.add(key_to_open_door(ord(key)))

        # initialize + open door with init-having keys
        for i in range(row):
            board[i + 1] = parse_board_row(board[i+1], open_doors)

        # check the walls and find open entries
        surroundings = get_surroundings(board)
        closed_door = dict()
        to_visit, visited = list(surroundings), set(surroundings)

        # run dfs
        while to_visit:
            vpos = to_visit.pop()
            vx, vy = vpos
            vcell = board[vx][vy]

            for wpos in get_adjacent(board, vpos):
                if wpos not in visited:
                    wcell = board[wpos[0]][wpos[1]]
                    if is_door_cell(wcell):
                        if wcell not in open_doors:
                            # if closed door - record & ignore
                            closed_door[wcell] = closed_door.get(wcell, []) + [wpos]
                            continue
                    elif is_key_cell(wcell):
                        new_door = key_to_open_door(wcell)
                        # if the key is new found key
                        if new_door not in open_doors:
                            # register key + for closed door previously, open it
                            open_doors.add(new_door)
                            for retry_pos in closed_door.get(new_door, []):
                                to_visit.append(retry_pos)
                                visited.add(retry_pos)
                    elif wcell == CELL_DOC:
                        document_count[-1] += 1

                    to_visit.append(wpos)
                    visited.add(wpos)

    print("\n".join(map(str, document_count)))


main()
