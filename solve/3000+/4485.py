# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
import heapq


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def get_next(vpos, size):
    x, y = vpos
    result = []
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < size and 0 <= ny < size:
            result.append((nx, ny))
    return result


def solve(board):
    """write your logic here"""
    size = len(board)
    starting = (0, 0)
    starting_cost = board[0][0]
    to_visit, visited = [(starting_cost, starting)], {starting: starting_cost}

    while to_visit:
        vdist, vpos = heapq.heappop(to_visit)

        if vdist > visited[vpos]:
            continue

        for wpos in get_next(vpos, size):
            wx, wy = wpos
            new_wdist = vdist + board[wx][wy]
            if (wpos not in visited) or (visited[wpos] > new_wdist):
                heapq.heappush(to_visit, (new_wdist, wpos))
                visited[wpos] = new_wdist

    return visited[(size - 1, size - 1)]


def test():
    """write your test here"""
    assert 1 == 1


def main():
    """write your i/o here"""
    problem_id = 0
    while (size := input_one(int)) != 0:
        problem_id += 1
        board = [None] * size
        for i in range(size):
            board[i] = input_list(int)

        print(f"Problem {problem_id}: {solve(board)}")


test()
main()
