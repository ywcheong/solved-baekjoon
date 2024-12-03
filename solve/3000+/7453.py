# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    size = input_one(int)
    A, B, C, D = ([None] * size for _ in range(4))

    for i in range(size):
        A[i], B[i], C[i], D[i] = input_list(int)

    CD = dict()
    for x in C:
        for y in D:
            CD[x + y] = CD.get(x + y, 0) + 1

    counter = 0
    for x in A:
        for y in B:
            counter += CD.get(-x - y, 0)

    print(counter)
    return counter


main()
