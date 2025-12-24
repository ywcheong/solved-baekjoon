# Implementation
def get_color(start_color, i, j):
    if start_color == 'B' and (i + j) % 2 == 0:
            return 'B'
    elif start_color == 'B' and (i + j) % 2 == 1:
            return 'W'
    elif start_color == 'W' and (i + j) % 2 == 0:
            return 'W'
    elif start_color == 'W' and (i + j) % 2 == 1:
            return 'B'
    else:
        raise Exception()

def get_subboard_paint(board, row_start, column_start, start_color):
    count = 0
    for row_pos in range(row_start, row_start + 8):
        for column_pos in range(column_start, column_start + 8):
            if board[row_pos][column_pos] != get_color(start_color, row_pos - row_start, column_pos - column_start):
                count += 1
    return count

def get_paint(board):
    row, column = len(board), len(board[0])
    result = 64

    for row_start in range(row-7):
        # [row_start ~ row_start+7]
        for column_start in range(column-7):
            # [column_start ~ column_start + 7]
            result = min(result, get_subboard_paint(board, row_start, column_start, 'B'))
            result = min(result, get_subboard_paint(board, row_start, column_start, 'W'))

    return result


# Testing
def to_board(text):
    return list(map(list, text.split('\n')))

def test():
    print("WARNING: TEST MODE")

    assert to_board('''WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW''') == [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'B', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
    
    assert get_paint(to_board('''BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB''')) == 12
    
    assert get_paint(to_board('''BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB''')) == 0
    
    assert get_paint(to_board('''BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBW''')) == 31
    
    assert get_paint(to_board('''BBBBBBBBBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBBBBBBBBB''')) == 0
    
    assert get_paint(to_board('''WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWWWB
BWBWBWBW''')) == 2
    
    assert get_paint(to_board('''BWWBWWBWWBWW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBWWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW''')) == 15

    print("TEST DONE")

# Submit
def submit():
    row, column = map(int, input().split())
    board = []

    for _ in range(row):
        board.append(list(input()))

    print(get_paint(board))

# Case-switch
if __name__ == '__main__':
    submit()