# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def is_explode(result, explode):
    if len(result) < len(explode):
        return False

    for i in range(len(explode)):
        if result[-i - 1] != explode[-i - 1]:
            return False

    return True


def remove_explode(result, explode):
    for _ in range(len(explode)):
        result.pop()


def main():
    """write your code here"""
    given_string = input_one(str)
    explode = input_one(str)

    result = []
    for char in given_string:
        result.append(char)
        while is_explode(result, explode):
            remove_explode(result, explode)

    return "".join(result) if len(result) > 0 else "FRULA"


print(main())
