# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


class Pos:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __lt__(self, other):
        if self.y != other.y:
            return self.y < other.y
        return self.x < other.x
    
    def __str__(self):
        return f"{self.x} {self.y}"


def solve(x):
    """write your solution here"""
    return x


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve(1), 1)
    check(solve(2), 2)
    check(solve(3), 3)


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    size = input_one(int)
    pos_list = [None] * size
    for i in range(size):
        pos_list[i] = Pos(*input_list(int))
    
    pos_list.sort()
    for pos in pos_list:
        print(pos)


# test()
main()
