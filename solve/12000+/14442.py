# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque
from typing import list

CLEAR = 0
WALL = 1

class State:
    xsize: int
    ysize: int

    @staticmethod
    def set_world(xsize, ysize):
        State.xsize = xsize
        State.ysize = ysize

    def __init__(self, x, y, breach):
        self.x = x
        self.y = y
        self.breach = breach

    def __repr__(self) -> str:
        return f"[x:{self.x}|y:{self.y}|b:{self.breach}]"

    def __hash__(self) -> int:
        return (self.x * State.ysize + self.y) * 10 + (self.breach - 1)

    def __eq__(self, other) -> bool:
        return self.x == other.x \
            and self.y == other.y \
            and self.breach == other.breach
    
    def is_goal(self):
        return self.x == State.xsize - 1 \
            and self.y == State.ysize - 1
    
    def get_nexts(self, board):
        result = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < State.xsize and 0 <= ny < State.ysize:
                if board[nx][ny] == WALL and self.breach > 0:
                    result.append(State(nx, ny, self.breach - 1))
                elif board[nx][ny] == CLEAR:
                    result.append(State(nx, ny, self.breach))
        return result


def solve(board, breach):
    """write your solution here"""
    xsize, ysize = len(board), len(board[0])
    State.set_world(xsize, ysize)
    
    start = State(0, 0, breach)
    to_visit, visited = deque([start]), {start: 1}

    while len(to_visit) > 0:
        vstate = to_visit.popleft()
        # print(f"visiting: {vstate} dist {visited[vstate]}")

        for wstate in vstate.get_nexts(board):
            if wstate not in visited:
                to_visit.append(wstate)
                visited[wstate] = visited[vstate] + 1
                if wstate.is_goal():
                    return visited[wstate]

    return -1

def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve([
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 0, 0, 0],
    ], 1), 15)
    check(solve([
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 0, 0, 0],
    ], 2), 9)
    check(solve([
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 0],
    ], 3), -1)


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    xsize, ysize, breach = input_list(int)
    board = [None] * xsize
    for x in range(xsize):
        row = list(input_one(str))
        row = list(map(int, row))
        board[x] = row
    print(solve(board, breach))


# test()
main()
