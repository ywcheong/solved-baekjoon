# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def add_city(mask, city_id):
    return mask | (1 << city_id)


def remove_city(mask, city_id):
    return mask & ~(1 << city_id)


def is_visited(mask, city_id):
    return bool(mask & (1 << city_id))


def main():
    """write your code here"""
    num_city = input_one(int)
    dist = [None] * num_city

    for i in range(num_city):
        dist[i] = input_list(int)

    for i in range(num_city):
        for j in range(num_city):
            if dist[i][j] == 0:
                dist[i][j] = float("inf")

    memo = [[None] * (2**num_city) for i in range(num_city)]

    empty_set = 0
    full_set = 2**num_city - 1

    def backtrack(state, current_city):
        if state == full_set:
            # try to move to start city, #0
            return dist[current_city][0]

        if (cache := memo[current_city][state]) is not None:
            # cache hit - memoization
            return cache

        known_min = float("inf")
        for next_city in range(num_city):
            #  ( already visited )          or  ( cannot visit from this city )
            if is_visited(state, next_city) or dist[current_city][next_city] == float(
                "inf"
            ):
                continue

            known_min = min(
                known_min,
                backtrack(add_city(state, next_city), next_city)
                + dist[current_city][next_city],
            )

        memo[current_city][state] = known_min
        return known_min

    start_city = 0
    start_set = add_city(empty_set, start_city)
    return backtrack(start_set, start_city)


print(main())
