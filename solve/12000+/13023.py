# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque


def solve(graph):
    """write your solution here"""

    def _backtrack(state):
        if len(state) == 5:
            return True

        last = state[-1]
        for w in graph[last]:
            if w not in state:
                if _backtrack(state + [w]):
                    return True

        return False

    for start in range(len(graph)):
        if _backtrack([start]):
            return True
    return False


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
    num_people, num_friends = input_list(int)
    friends = [list() for i in range(num_people)]
    for _ in range(num_friends):
        this, that = input_list(int)
        friends[this].append(that)
        friends[that].append(this)
    print(int(solve(friends)))


main()
