# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    #
    # 1 /  | x1 x2 ... xn x1 |
    #  / 2 | y1 y2 ... yn y1 |
    size = input_one(int)
    x_list, y_list = [None] * size, [None] * size
    
    for i in range(size):
        x_list[i], y_list[i] = input_list(int)

    result = 0

    for x, y in zip(x_list, y_list[1:] + y_list[:1]):
        result += x * y

    for x, y in zip(x_list[1:] + x_list[:1], y_list):
        result -= x * y

    result = abs(result) / 2

    print(f"{result:.1f}")


main()
