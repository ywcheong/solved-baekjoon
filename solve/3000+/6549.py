# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


MOVE_LEFT, MOVE_RIGHT = -5, -7


def solve(heights, lo, hi):
    """write your logic here"""
    if lo == hi:
        return heights[lo]

    mid = (lo + hi) // 2
    result = solve(heights, lo, mid)
    result = max(result, solve(heights, mid + 1, hi))

    left, right = mid, mid + 1
    current_height = min(heights[left], heights[right])
    max_area = (right - left + 1) * current_height
    while True:
        move_mode = None
        if lo < left and right < hi:
            if heights[left-1] < heights[right+1]:
                move_mode = MOVE_RIGHT
            else:
                move_mode = MOVE_LEFT
        elif lo < left:
            move_mode = MOVE_LEFT
        elif right < hi:
            move_mode = MOVE_RIGHT
        else:
            break

        # recompute
        if move_mode == MOVE_LEFT:
            left -= 1
            current_height = min(current_height, heights[left])
        elif move_mode == MOVE_RIGHT:
            right += 1
            current_height = min(current_height, heights[right])
        else:
            raise ValueError("No move mode")

        max_area = max(max_area, (right - left + 1) * current_height)

    result = max(result, max_area)
    return result


def test():
    """write your test here"""
    assert solve([2, 1, 4, 5, 1, 3, 3], 0, 6) == 8
    assert solve([1000, 1000, 1000, 1000], 0, 3) == 4000


def main():
    """write your i/o here"""
    while True:
        heights = input_list(int)
        if len(heights) == 1:
            break
        print(solve(heights[1:], 0, len(heights) - 2))


# test()
main()
