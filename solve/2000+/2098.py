# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    num_city = input_one(int)

    weight = [None] * num_city
    for i in range(num_city):
        weight[i] = input_list(int)

    heuristic = [None] * num_city
    for end in range(num_city):
        heuristic[end] = min(
            filter(
                lambda dist: dist > 0, [weight[start][end] for start in range(num_city)]
            )
        )
    sum_heuristic = sum(heuristic)

    known_shortest = float("inf")

    def backtrack(visited, start_city, this_city, dist):
        nonlocal known_shortest

        if len(visited) == num_city:
            back_dist = weight[this_city][start_city]
            if back_dist != 0:
                known_shortest = min(known_shortest, dist + back_dist)
            return

        heuristic_dist = dist + sum_heuristic + heuristic[start_city]
        for city in visited:
            heuristic_dist -= heuristic[city]

        # print(
        #     f"visited={visited}, start_city={start_city}, this_city={this_city}, dist={dist}, heuristic_dist={heuristic_dist} known_shortest={known_shortest}"
        # )
        
        if heuristic_dist >= known_shortest:
            return

        for next_city in range(num_city):
            next_dist = weight[this_city][next_city]

            if (
                (next_dist == 0)
                or (next_city in visited)
                or (dist + next_dist > known_shortest)
            ):
                continue

            visited.add(next_city)
            backtrack(visited, start_city, next_city, dist + next_dist)
            visited.remove(next_city)

    for start_city in range(num_city):
        backtrack({start_city}, start_city, start_city, 0)

    print(known_shortest)


main()
