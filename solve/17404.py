# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


NUM_COLOR = 3

def main():
    """write your code here"""
    size = input_one(int)
    cost = [None] * size

    for i in range(size):
        cost[i] = input_list(int)

    # memo[i][c]: For cost[:i+1], when last house color = c, the coloring cost.
    memo = [[None]*3 for _ in range(size)]
    known_min = float("inf")
    
    color_set = {0, 1, 2}
    for start_color in range(NUM_COLOR):
        # Initializing: memo[1]: For starting color it is impossible
        for non_start_color in color_set - {start_color}:
            memo[1][non_start_color] = cost[0][start_color] + cost[1][non_start_color]
        memo[1][start_color] = float("inf")

        for i in range(2, size):
            memo[i][0] = cost[i][0] + min(memo[i-1][1], memo[i-1][2])
            memo[i][1] = cost[i][1] + min(memo[i-1][0], memo[i-1][2])
            memo[i][2] = cost[i][2] + min(memo[i-1][0], memo[i-1][1])

        for non_start_color in color_set - {start_color}:
            known_min = min(known_min, memo[-1][non_start_color])

    print(known_min)
    return


main()
