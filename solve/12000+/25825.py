# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


SIZE = 12
PINF = float("inf")

EMPTY_SET = 0
FULL_SET = 2**SIZE - 1


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def add_set(bitset, element):
    return bitset | (1 << element)


def remove_set(bitset, element):
    return bitset & ~(1 << element)


def is_contain(bitset, element):
    return bool(bitset & (1 << element))


def solve(board):
    """write your logic here"""
    # memo[pos][board] = RESULT
    memo = [[None] * 2**SIZE for _ in range(SIZE)]

    def get_friend(pos):
        if pos % 2 == 0:
            return pos + 1
        return pos - 1

    def _backtrack(pos, visited_set):
        if visited_set == FULL_SET:
            return 0
        if (cache := memo[pos][visited_set]) is not None:
            return cache

        result = PINF
        friend = get_friend(pos)

        if not is_contain(visited_set, friend):
            result = (
                _backtrack(friend, add_set(visited_set, friend)) + board[pos][friend]
            )
        else:
            for next_pos in range(SIZE):
                if is_contain(visited_set, next_pos):
                    continue

                result = min(
                    result,
                    _backtrack(next_pos, add_set(visited_set, next_pos))
                    + board[pos][next_pos],
                )

        memo[pos][visited_set] = result
        return result

    result = PINF
    for start in range(SIZE):
        result = min(result, _backtrack(start, add_set(EMPTY_SET, start)))

    return result


def main():
    """write your i/o here"""
    board = [None] * SIZE
    for i in range(SIZE):
        board[i] = input_list(int)
    print(solve(board))


main()
