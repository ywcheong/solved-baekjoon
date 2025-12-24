# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    size, memory_goal = input_list(int)
    memory_list = input_list(int)
    cost_list = input_list(int)

    if size == 1:
        return cost_list[0]

    # memo[end_index][cost] = MEMORY
    memo = [[float("inf")] * 10001 for _ in range(size)]
    memo[0] = [(memory_list[0] if cost >= cost_list[0] else 0) for cost in range(10001)]

    known_min_cost = float("inf")

    for end_index in range(1, size):
        current_cost = cost_list[end_index]
        current_memory = memory_list[end_index]
        for cost in range(10001):
            if cost >= current_cost:
                memo[end_index][cost] = max(
                    memo[end_index - 1][cost],
                    memo[end_index - 1][cost - current_cost] + current_memory,
                )
            else:
                memo[end_index][cost] = memo[end_index - 1][cost]
            if memo[end_index][cost] >= memory_goal:
                known_min_cost = min(known_min_cost, cost)

    return known_min_cost


print(main())
