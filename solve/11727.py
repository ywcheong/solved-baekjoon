# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from typing import List


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input().split()))


""" write your code here """
def main():
    n = input_one(int)
    if n == 1:
        print(1)
        return
    elif n == 2:
        print(3)
        return
    
    result = [None] * (n + 1)
    result[1:3] = [1, 3]

    for i in range(3, n+1):
        result[i] = (result[i-1] + 2 * result[i-2]) % 10007
    
    print(result[-1])


main()