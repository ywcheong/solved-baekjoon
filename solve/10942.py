# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    n = input_one(int)
    L = input_list(int)
    assert n == len(L)

    # is_mirror[i][j] == is_palindrome(L[i:j+1])
    is_mirror = [[None] * n for _ in range(n)]

    for start in range(n):
        end = start + 0
        is_mirror[start][end] = True
    
    for start in range(n-1):
        end = start + 1
        is_mirror[start][end] = (L[start] == L[end])

    for length in range(2, n):
        for start in range(n-length):
            end = start + length
            is_mirror[start][end] = is_mirror[start+1][end-1] and (L[start] == L[end])
    
    query_count = input_one(int)
    for _ in range(query_count):
        query_start, query_end = input_list(int)
        print(int(is_mirror[query_start-1][query_end-1]))


main()
