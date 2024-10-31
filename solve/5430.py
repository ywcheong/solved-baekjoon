# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque


class ACLanguage:
    def __init__(self, L):
        self.L = deque(L)
        self.is_error = False
        self.is_front = True

    def __str__(self):
        if self.is_error:
            return "error"
        if self.is_front:
            return f"""[{",".join(map(str, self.L))}]"""
        return f"""[{",".join(map(str, reversed(self.L)))}]"""

    def __len__(self):
        return len(self.L)

    def feed_function(self, functions):
        for func in list(functions):
            if func == "R":
                self.reverse()
            elif func == "D":
                self.drop()
            else:
                raise ValueError()

    def reverse(self):
        if self.is_error:
            return
        self.is_front = not self.is_front

    def drop(self):
        if self.is_error:
            return
        if len(self) == 0:
            self.is_error = True
            return

        if self.is_front:
            self.L.popleft()
        else:
            self.L.pop()


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    testcase_count = input_one(int)
    for _ in range(testcase_count):
        functions = input_one(str)
        _ = input_one(str)
        given_list = input_one(str)
        if given_list == "[]":
            L = []
        else:
            L = list(map(int, given_list[1:-1].split(",")))
        aclang = ACLanguage(L)
        aclang.feed_function(functions)
        print(aclang)


main()
