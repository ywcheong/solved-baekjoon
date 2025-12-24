# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
import heapq

WALL = "*"
EMPTY = "."
CPOINT = "C"

PINF = float("inf")


class State:
    DIRECTIONS = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

    @staticmethod
    def create_from(pos):
        x, y = pos
        return [State(x, y, each_dir) for each_dir in State.DIRECTIONS]

    def __init__(self, x, y, dir):
        self.x, self.y, self.dir = x, y, dir

    def get_next(self, board):
        xsize, ysize = len(board), len(board[0])
        result = []

        # Changed direction
        for other_dir in State.DIRECTIONS:
            if other_dir != self.dir:
                result.append((1, State(self.x, self.y, other_dir)))

        # Changed pos
        next_x, next_y = self.x + self.dir[0], self.y + self.dir[1]

        if 0 <= next_x < xsize and 0 <= next_y < ysize and board[next_x][next_y] != WALL:
            result.append((0, State(next_x, next_y, self.dir)))

        return result

    def is_pos(self, pos):
        other_x, other_y = pos
        return self.x == other_x and self.y == other_y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.dir == other.dir
    
    def __hash__(self):
        return hash((self.x, self.y, self.dir))
    
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        
        if self.y != other.y:
            return self.y < other.y
        
        return self.dir < other.dir
    
    def __repr__(self):
        return f"<x={self.x},y={self.y},dir={self.dir}>"


def find_two_poses(board):
    pos1, pos2 = None, None

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == CPOINT:
                if pos1 is None:
                    pos1 = (x, y)
                else:
                    pos2 = (x, y)

    return pos1, pos2


def dijkstra(start_pos, goal_pos, board):
    starts = State.create_from(start_pos)
    to_visit = [(0, start) for start in starts]
    visited = {start: 0 for start in starts}

    # print(f"Find {start_pos} -> {goal_pos}")

    while to_visit:
        vdist, vstate = heapq.heappop(to_visit)
        # print(f"visit: vstate={vstate} vdist={vdist} ->")

        # 이미 더 짧은 경로가 알려진 노드라면: 탐색 중단
        if visited.get(vstate, PINF) < vdist:
            continue

        if vstate.is_pos(goal_pos):
            return visited[vstate]

        for weight, wstate in vstate.get_next(board):
            wdist = vdist + weight
            # print(f"-- wstate={wstate} wdist={wdist}")
            # (아직 발견되지 않았거나) or (발견되었음에도 개선가능하면) 갱신
            if (wstate not in visited) or (wdist < visited[wstate]):
                # print("-- ^ !!!")
                heapq.heappush(to_visit, (wdist, wstate))
                visited[wstate] = wdist

    assert False, "Problem guarantees that two points are always connectable"


def solve(board):
    """write your solution here"""
    pos_start, pos_goal = find_two_poses(board)
    return dijkstra(pos_start, pos_goal, board)


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(
        solve(
            [
                ".......",
                ".....CC",
                "......*",
                "*****.*",
                "....*..",
                "....*..",
                "....*..",
                ".......",
            ]
        ),
        0,
    )
    check(
        solve(
            [
                ".......",
                "C.....C",
                "......*",
                "*****.*",
                "....*..",
                "....*..",
                "....*..",
                ".......",
            ]
        ),
        0,
    )
    check(
        solve(
            [
                "......C",
                "......C",
                "......*",
                "*****.*",
                "....*..",
                "....*..",
                "....*..",
                ".......",
            ]
        ),
        0,
    )
    check(
        solve(
            [
                ".......",
                "......C",
                "......*",
                "*****.*",
                "....*..",
                "....*C.",
                "....*..",
                ".......",
            ]
        ),
        1,
    )
    check(
        solve(
            [
                ".......",
                "......C",
                "......*",
                "*****.*",
                "....*..",
                "....*..",
                "....*..",
                "..C....",
            ]
        ),
        2,
    )
    check(
        solve(
            [
                ".......",
                "......C",
                "......*",
                "*****.*",
                "....*..",
                "....*..",
                ".C..*..",
                ".......",
            ]
        ),
        3,
    )


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    ysize, xsize = input_list(int)
    board = [None] * xsize
    for x in range(xsize):
        board[x] = input_one(str)
    print(solve(board))


# test()
main()
