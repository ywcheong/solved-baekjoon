# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from typing import List, Tuple
from collections import deque


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input().split()))


""" write your code here """
class State:

    board: List[List[int]]
    row_limit: int
    column_limit: int

    @classmethod
    def link_board(cls, board):
        cls.board = board
        cls.row_limit = len(board)
        cls.column_limit = len(board[0])

    def __init__(self, pos: Tuple[int], is_breakable: bool):
        self.pos = pos
        self.is_breakable = is_breakable
        self.obj_hash = hash((self.pos, self.is_breakable))

    def is_goal(self):
        return self.pos[0] == State.row_limit-1 and self.pos[1] == State.column_limit-1
    
    @classmethod
    def is_valid_pos(cls, i, j):
        return 0 <= i < cls.row_limit and 0 <= j < cls.column_limit

    def get_next_state(self):
        i, j = self.pos
        next_state_list = []

        for next_i, next_j in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if not State.is_valid_pos(next_i, next_j):
                continue

            if State.board[next_i][next_j] == "0":
                next_state_list.append(State(
                    pos=(next_i, next_j),
                    is_breakable=self.is_breakable
                ))
            elif self.is_breakable:
                next_state_list.append(State(
                    pos=(next_i, next_j),
                    is_breakable=False
                ))

        return next_state_list
    
    def __hash__(self):
        return self.obj_hash
    
    def __eq__(self, that):
        return self.pos == that.pos and self.is_breakable == that.is_breakable
    
    def __str__(self):
        return f"State[pos={self.pos}, ib={self.is_breakable}]"


def main():
    # row_limit, column_limit = input_list(int)
    # board = [None] * row_limit

    # for i in range(row_limit):
    #     board[i] = list(input_one(str))
    board = [["0"]*1000]*1000

    State.link_board(board)
    start_state = State(pos=(0,0), is_breakable=True)
    to_visit, visited = deque([start_state]), {start_state: 1}

    while to_visit:
        this_state = to_visit.popleft()
        # print(f"CurrentState={this_state} | toVisitLength={len(to_visit)} | visitedLength={len(visited)}")

        for next_state in this_state.get_next_state():
            if next_state not in visited:
                to_visit.append(next_state)
                visited[next_state] = visited[this_state] + 1
                if next_state.is_goal():
                    print(visited[next_state])
                    return
                
    print(-1)
    return

import cProfile
cProfile.run('main()')