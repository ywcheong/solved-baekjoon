# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


class SegmentTree:
    def __init__(self, L, operator, identity):
        self.size = len(L)
        self.tree = [None] * (self.size * 2)
        self.operator = operator
        self.identity = identity

        # Load data into [+size] frame
        for i in range(self.size):
            self.tree[i + self.size] = L[i]

        # Compute [-size] frame
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.operator(
                self.tree[i << 1 | 0],
                self.tree[i << 1 | 1],
            )

    def update(self, index, value):
        # Change into [+size] frame
        index = index + self.size
        self.tree[index] = value

        # update recursively
        while index > 1:
            index >>= 1
            self.tree[index] = self.operator(
                self.tree[index << 1 | 0], self.tree[index << 1 | 1]
            )

    def range(self, left, right):
        # Change into [+size] frame
        left += self.size
        right += self.size
        result = self.identity

        while left < right:
            if left & 1:
                result = self.operator(result, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                result = self.operator(result, self.tree[right])
            left >>= 1
            right >>= 1

        return result


def main():
    """write your code here"""
    size, num_change, num_range = input_list(int)
    L = [None] * size

    for i in range(size):
        L[i] = input_one(int)

    def mult(a, b):
        return (a * b) % 1_000_000_007

    segtree = SegmentTree(L, mult, 1)

    UPDATE_COMMAND, RANGE_COMMAND = (
        1,
        2,
    )

    for _ in range(num_change + num_range):
        argv = input_list(int)

        if argv[0] == UPDATE_COMMAND:
            segtree.update(argv[1] - 1, argv[2])
        elif argv[0] == RANGE_COMMAND:
            print(segtree.range(argv[1] - 1, argv[2]))
        else:
            raise NotImplementedError("unknown command")


main()
