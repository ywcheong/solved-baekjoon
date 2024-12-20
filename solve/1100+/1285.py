# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys

def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def add_set(bitset, element):
    return bitset | (1 << element)


def remove_set(bitset, element):
    return bitset & ~(1 << element)


def is_contain(bitset, element):
    return bool(bitset &  (1 << element))


def solve(board):
    """write your logic here"""
    size = len(board)
    empty_set = 0
    full_set = 2 ** size - 1
    upper_limit = full_set + 1

    def count_value(value):
        count = 0
        while value > 0:
            count += (value % 2)
            value //= 2
        return count

    result = size ** 2 + 1
    for column in range(empty_set, upper_limit):
        trial_value = 0
        for row in board:
            row_count = count_value((row ^ column) & full_set)
            trial_value += min(row_count, size - row_count)
        result = min(result, trial_value)

    return result


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(solve([0b001, 0b100, 0b101]), 2)


def main():
    """write your i/o here"""
    size = input_one(int)
    board = [None] * size

    value_dict = {'H': 0, 'T': 1}

    def line_to_value(line):
        result = 0
        for i, x in enumerate(reversed(line)):
            result += (2 ** i) * value_dict[x]
        return result

    for i in range(size):
        line = input_one(str)
        board[i] = line_to_value(line)

    print(solve(board))


# test()
main()
