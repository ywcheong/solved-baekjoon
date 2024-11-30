# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(first: str, second: str, third: str):
    next = None

    if first.isdigit():
        next = int(first) + 3
    elif second.isdigit():
        next = int(second) + 2
    elif third.isdigit():
        next = int(third) + 1
    else:
        assert False, "??"

    if next % 15 == 0:
        return "FizzBuzz"
    elif next % 3 == 0:
        return "Fizz"
    elif next % 5 == 0:
        return "Buzz"
    else:
        return next

def test():
    """write your test here"""
    assert 1 == 1


def main():
    """write your i/o here"""
    first, second, third = input_one(str), input_one(str), input_one(str)
    print(solve(first, second, third))


test()
main()
