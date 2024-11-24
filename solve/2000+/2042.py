# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


class SegmentTree:
    def __init__(self, L, operator, identity):
        self.size = len(L)
        self.operator = operator
        self.identity = identity
        self.tree = [None] * (2 * self.size)

        # Load the data to [+size] frame
        for i in range(self.size):
            self.tree[self.size + i] = L[i]

        # Fill the tree into [-size] frame
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.operator(self.tree[i << 1], self.tree[i << 1 | 1])

    def update(self, index, value):
        ''' update[index => value] '''
        # Prepare index to [+size] frame
        index += self.size

        # update value
        self.tree[index] = value

        while index > 1:
            # move to parent, and update it
            index >>= 1
            self.tree[index] = self.operator(
                self.tree[index << 1],
                self.tree[index << 1 | 1],
            )

    def range(self, left, right):
        ''' range:[left, right) '''
        # Prepare index to [+size] frame
        left += self.size
        right += self.size

        # Compute the result, from identity
        result = self.identity

        while left < right:
            # If left is right-leaf, add and jump right
            if left & 1:
                result = self.operator(result, self.tree[left])
                left += 1   # right-of-parent
            # If right
            if right & 1:
                right -= 1
                result = self.operator(result, self.tree[right])
            left >>= 1
            right >>= 1
        return result
    
    def __str__(self):
        return str(self.tree[self.size:])


UPDATE_COMMAND, RANGE_COMMAND = 1, 2


def main():
    """write your code here"""
    size, num_update, num_range = input_list(int)
    num_command = num_update + num_range

    L = [None] * size
    for i in range(size):
        L[i] = input_one(int)

    segtree = SegmentTree(
        L,
        int.__add__,  # addition (this satisfies assosiation over integers)
        0,  # You know, according to the math, zero is the addition identity
    )

    for _ in range(num_command):
        command, arg1, arg2 = input_list(int)
        if command == UPDATE_COMMAND:
            segtree.update(arg1 - 1, arg2)
        elif command == RANGE_COMMAND:
            # range:[arg1, arg2] = range:[arg1, arg2 + 1)
            print(segtree.range(arg1 - 1, (arg2 - 1) + 1))
        else:
            raise NotImplementedError("unknown command")

main()
