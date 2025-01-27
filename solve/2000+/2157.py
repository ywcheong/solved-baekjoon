# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys

INF = float("inf")


def route_to_graph(num_city, routes):
    graph = dict()

    for start_city, end_city, meal_score in routes:
        if end_city <= start_city:
            continue

        # 가장 맛있는 기내식만 계산하자!
        graph[start_city, end_city] = max(
            graph.get((start_city, end_city), -INF), meal_score
        )

    return graph


def solve(num_city, max_visit_city, routes):
    """write your solution here"""

    graph = route_to_graph(num_city, routes)
    memo = dict()

    def _recursion(this_city, remain_cities):
        # 도시 방문
        remain_cities -= 1

        # 1. Basis Step 처리
        # -- cache 처리 가능하면, cache 사용
        if (cache := memo.get((this_city, remain_cities), None)) is not None:
            return cache

        # -- 이 경로가 불가능하면, 기내식 점수를 무효화
        if remain_cities < 0:
            return -INF

        # -- 이 도시가 마지막 도시면, 평가 종료
        if this_city == num_city:
            return 0

        # 2. Inductive Step 처리
        result = -INF
        for next_city in range(this_city + 1, num_city + 1):
            meal_score = graph.get((this_city, next_city), None)
            if meal_score is not None:
                score = meal_score + _recursion(next_city, remain_cities)
                result = max(result, score)

        # 3. 캐시 처리 후 반환
        memo[this_city, remain_cities] = result
        return result

    return _recursion(1, max_visit_city)


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    num_city, max_visit_city, num_route = input_list(int)

    routes = [None] * num_route
    for i in range(num_route):
        routes[i] = input_list(int)

    print(solve(num_city, max_visit_city, routes))


main()
