# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


PINF = float("inf")


def reachable_from_source(edges, source):
    to_visit, visited = [source], {source}
    while to_visit:
        v = to_visit.pop()

        for start, end, _ in edges:
            if start == v and end not in visited:
                to_visit.append(end)
                visited.add(end)

    return visited


def reachable_to_dest(edges, dest):
    to_visit, visited = [dest], {dest}
    while to_visit:
        v = to_visit.pop()

        for start, end, _ in edges:
            if end == v and start not in visited:
                to_visit.append(start)
                visited.add(start)

    return visited


def bellman_ford(nodes, edges, start):
    visited = {v: PINF for v in nodes}
    visited[start] = 0

    # Vue: For v iteration...
    for update_iteration in range(1, len(nodes) + 1):
        # vUE: Update Edges, but visited one
        for start, end, weight in edges:
            if visited[start] == PINF:
                continue

            new_dist = visited[start] + weight
            if new_dist < visited[end]:
                visited[end] = new_dist

                if update_iteration == len(nodes):
                    raise ValueError("Negative cycle exists")

    return visited


def main():
    """write your code here"""
    num_city, city_start, city_end, num_edge = input_list(int)
    edges = [None] * num_edge

    for i in range(num_edge):
        # (start, end, weight)
        edges[i] = input_list(int)

    city_earnings = input_list(int)
    assert len(city_earnings) == num_city

    for i in range(num_edge):
        start, end, weight = edges[i]
        edges[i] = start, end, weight - city_earnings[end]

    start_nodes = reachable_from_source(edges, city_start)
    end_nodes = reachable_to_dest(edges, city_end)
    common_nodes = start_nodes & end_nodes

    if len(common_nodes) == 0:
        print("gg")
        return

    common_edges = []
    for start, end, weight in edges:
        if start in common_nodes and end in common_nodes:
            common_edges.append((start, end, weight))

    try:
        shortest = bellman_ford(common_nodes, common_edges, city_start)
        print(-shortest[city_end] + city_earnings[city_start])
    except ValueError as e:
        print("Gee")


main()
