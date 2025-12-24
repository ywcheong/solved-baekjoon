# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def get_digit(num, pos):
    return (num // 10**pos) % 10


def is_mirror(num, size):
    for i in range(size // 2 + 1):
        if get_digit(num, i) != get_digit(num, size - 1 - i):
            return False
    return True


def solve(line):
    """write your logic here"""
    size = len(line)
    num = int(line)
    while not is_mirror(num, size):
        num += 1
    return num - int(line)


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(is_mirror(123, 3), False)
    check(is_mirror(121, 3), True)
    check(is_mirror(120, 4), False)
    check(is_mirror(110, 4), True)
    check(is_mirror(1234, 4), False)
    check(is_mirror(1223, 4), False)
    check(is_mirror(1221, 4), True)

    print("=========")

    check(solve("100000"), 1)
    check(solve("100001"), 0)
    check(solve("000121"), 979)
    check(solve("00456"), 44)


def main():
    """write your i/o here"""
    while (line := input_one(str)) != "0":
        print(solve(line))


# test()
main()
