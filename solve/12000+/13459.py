# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque

VOID = "."
WALL = "#"
HOLE = "O"
RED_BALL = "R"
BLUE_BALL = "B"

DEPTH_LIMIT = 10

def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(board):
    """
        1. Put the red ball into the hole
        2. Do not put the blue ball into the hole
        3. Do this within 10 tilts.
    """
    DIM1, DIM2 = len(board), len(board[0])
    red_pos, blue_pos, goal_pos = None, None, None

    # 1. Find intial red/blue pos
    for i in range(DIM1):
        for j in range(DIM2):
            if board[i][j] == RED_BALL:
                red_pos = (i, j)
            elif board[i][j] == BLUE_BALL:
                blue_pos = (i, j)
            elif board[i][j] == HOLE:
                goal_pos = (i, j)

    # 2. Conduct BFS of depth 10

    # 2.1. BFS supplementary function - compute next possible ball positions
    def compute_next(ball_poses):
        result = []

        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            red_pos, blue_pos = ball_poses

            # To simulate: Simulate red, then blue, then red
            # This is identical with simulating both red and blue
            red_pos = simulate_movement(red_pos, direction, blue_pos)
            blue_pos = simulate_movement(blue_pos, direction, red_pos)
            red_pos = simulate_movement(red_pos, direction, blue_pos)
            
            # For ->, <-, V, ^: there are three possible outcomes
            if blue_pos == goal_pos:
                # 1. Blue ball fall into hole : Fail
                pass
            elif red_pos == goal_pos:
                # 2. Red ball fall into hole : Success
                result.append((True, (red_pos, blue_pos)))
            else:
                # 3. Nothing : Continue
                result.append((False, (red_pos, blue_pos)))
        
        # print(f"[CmpNext] Pos: [{ball_poses}], Next: [{result}]")

        return result
    
    def simulate_movement(pos, direction, other_ball_pos):
        # 1. If thispos == goal, return
        # 2. If next is ball, or wall, stop and return
        # 3. If next is void, proceed
        di, dj = direction
        i, j = pos
        # print(f"[SimMove] Start [{i}, {j}] + Direction [{di}, {dj}]")

        while True:
            if (i, j) == goal_pos:
                # print(f"[SimMove] Goal Halt [{i}, {j}]")
                return (i, j)
            
            ni, nj = i + di, j + dj
            if board[ni][nj] == WALL or ((ni, nj) == other_ball_pos and (ni, nj) != goal_pos):
                # print(f"[SimMove] Wall Halt [{i}, {j}]")
                return (i, j)
            
            # print(f"[SimMove] Move [{i}, {j}] -> [{ni}, {nj}]")
            i, j = ni, nj

        # Since the board is surrounded with wall, this statement is unreachable
        raise AssertionError("Cannot reach this statement")

    # 2.2. BFS main logic
    starting = (red_pos, blue_pos)
    to_visit, visited = deque([starting]), {starting: 0}

    while to_visit:
        ball_poses = to_visit.popleft()
        current_level = visited[ball_poses]
        # print(f"[BFS    ] Pos: [{ball_poses}], Depth: [{current_level}]")

        # Level 10 is already verified in Level 9
        if visited[ball_poses] == DEPTH_LIMIT:
            return False
        
        for is_success, next_poses in compute_next(ball_poses):
            # For level L, verify and search L+1
            if is_success and current_level <= DEPTH_LIMIT - 1:
                return True
            
            if current_level <= DEPTH_LIMIT - 1 and next_poses not in visited:
                to_visit.append(next_poses)
                visited[next_poses] = current_level + 1

    return False


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    
    # Testcase 1
    check(solve([
        "#####",
        "#..B#",
        "#.#.#",
        "#RO.#",
        "#####",
    ]), True)

    # Testcase 2
    check(solve([
        "#######",
        "#...RB#",
        "#.#####",
        "#.....#",
        "#####.#",
        "#O....#",
        "#######",
    ]), True)

    # Testcase 3
    check(solve([
        "#######",
        "#..R#B#",
        "#.#####",
        "#.....#",
        "#####.#",
        "#O....#",
        "#######",
    ]), True)

    # Testcase 4
    check(solve([
        "##########",
        "#R#...##B#",
        "#...#.##.#",
        "#####.##.#",
        "#......#.#",
        "#.######.#",
        "#.#....#.#",
        "#.#.#.#..#",
        "#...#.O#.#",
        "##########",
    ]), False)

    # Testcase 5
    check(solve([
        "#######",
        "#R.O.B#",
        "#######",
    ]), True)

    # Testcase 6
    check(solve([
        "##########",
        "#R#...##B#",
        "#...#.##.#",
        "#####.##.#",
        "#......#.#",
        "#.######.#",
        "#.#....#.#",
        "#.#.##...#",
        "#O..#....#",
        "##########",
    ]), True)

    # Testcase 7
    check(solve([
        "##########",
        "#.O....RB#",
        "##########",
    ]), False)


def main():
    """write your i/o here"""
    height, width = input_list(int)
    board = [None] * height
    for i in range(height):
        board[i] = input_one(str)
    print(int(solve(board)))


# test()
main()
