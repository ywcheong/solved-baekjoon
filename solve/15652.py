# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys

# 자연수 N과 K이 주어졌을 때, 아래 조건을 만족하는 길이가 K인 수열을 모두 구하는 프로그램을 작성하시오.

#     1부터 N까지 자연수 중에서 K개를 고른 수열
#     같은 수를 여러 번 골라도 된다.
#     고른 수열은 비내림차순이어야 한다.
#         길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    N, K = input_list(int)

    def backtrack(state):
        if len(state) == K:
            print(" ".join(map(str, state)))
            return

        begin = 1
        if len(state) > 0:
            begin = state[-1]
        for next_num in range(begin, N + 1):
            state.append(next_num)
            backtrack(state)
            state.pop()

    backtrack([])


main()
