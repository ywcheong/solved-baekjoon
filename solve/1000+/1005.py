# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
import heapq


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


FLOWIN = 1000000
FLOWOUT = 2000000


def get_shortest(start, edge):
    to_visit, visited = [(0, start)], {start: 0}
    farthest = 0

    while to_visit:
        dist, v = heapq.heappop(to_visit)

        # 만료된 노드 제거
        if dist > visited[v]:
            continue

        farthest = min(farthest, dist)

        for weight, w in edge[v]:
            # (미개척) or (더 나은 개척)
            new_dist = dist + weight
            if w not in visited or new_dist < visited[w]:
                heapq.heappush(to_visit, (new_dist, w))
                visited[w] = new_dist

    return -farthest


def main():
    """write your code here"""
    testcase_count = input_one(int)
    for _ in range(testcase_count):
        build_count, rule_count = input_list(int)
        build_list = input_list(int)
        assert len(build_list) == build_count

        rule_list: dict[int, list[tuple[int, int]]] = dict()
        for node in range(1, build_count + 1):
            rule_list[node + FLOWIN] = [(-build_list[node - 1], node + FLOWOUT)]
            rule_list[node + FLOWOUT] = []

        for _ in range(rule_count):
            start, end = input_list(int)
            rule_list[end + FLOWOUT].append((0, start + FLOWIN))

        target_building = input_one(int)
        print(get_shortest(FLOWIN + target_building, rule_list))


main()
