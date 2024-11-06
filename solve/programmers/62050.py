import itertools, heapq
from collections import deque

INFINITY = float("inf")


def solution(land, height):
    size = len(land)

    def compute_adj_pos(pos):
        """Return adjacent pos from given `pos`"""
        x, y = pos
        result = []
        for px, py in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= px < size and 0 <= py < size:
                result.append((px, py))
        return result

    def compute_next_pos(pos):
        """Return next possible pos from given `pos`"""
        x, y = pos
        result = []
        for px, py in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (
                0 <= px < size
                and 0 <= py < size
                and abs(land[x][y] - land[px][py]) <= height
            ):
                result.append((px, py))
        return result

    def classify_land(land):
        """classify the given land into intermovable subgroups"""
        group_id = 0
        group = [[None] * size for _ in range(size)]
        not_visited = {(x, y) for x, y in itertools.product(range(size), range(size))}

        while not_visited:  # Start of each subgroup
            starting = not_visited.pop()
            to_visit = deque([starting])
            group[starting[0]][starting[1]] = group_id

            while to_visit:
                pos = to_visit.popleft()

                for next_pos in compute_next_pos(pos):
                    if next_pos in not_visited:
                        x, y = next_pos
                        group[x][y] = group_id
                        to_visit.append(next_pos)
                        not_visited.remove(next_pos)

            # increase group id by 1
            group_id += 1

        return group_id, group

    def compute_next_pos(pos):
        """Return next possible pos from given `pos`"""
        x, y = pos
        result = []
        for px, py in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (
                0 <= px < size
                and 0 <= py < size
                and abs(land[x][y] - land[px][py]) <= height
            ):
                result.append((px, py))
        return result

    def compute_group_cost(num_group, group_map):
        """Compute the cost[i][j] == (ladder-placing cost between group i and j)"""
        group_cost = [dict() for _ in range(num_group)]

        for ax, ay in itertools.product(range(size), range(size)):
            for bx, by in compute_adj_pos((ax, ay)):
                # same group, nevermind
                agroup, bgroup = group_map[ax][ay], group_map[bx][by]
                if agroup == bgroup:
                    continue
                cost = min(group_cost[agroup].get(bgroup, INFINITY), abs(land[ax][ay] - land[bx][by]))
                group_cost[agroup][bgroup], group_cost[bgroup][agroup] = cost, cost

        return group_cost

    def matrix_to_edges(num_node, graph):
        edges = []
        for x in range(num_node):
            for y in graph[x]:
                edges.append((graph[x][y], x, y))
        return edges

    def compute_mst(num_node, edges):
        """Given # node and adjacency matrix, compute MST with smallest weight sum using Kruskal"""
        edges.sort(reverse=True)

        mst = []
        parent = [x for x in range(num_node)]

        def get_root(x):
            if parent[x] == x:
                return x
            parent[x] = get_root(parent[x])
            return parent[x]

        def union_root(x, y):
            x, y = get_root(x), get_root(y)
            if x != y:
                parent[y] = x

        while len(mst) < num_node - 1:
            weight, v, w = edges.pop()

            # Not cycle-making
            if get_root(v) != get_root(w):
                mst.append(weight)
                union_root(v, w)

        return sum(mst)

    # classify land
    num_group, group_map = classify_land(land)

    # calculate cost between every groups
    group_cost = compute_group_cost(num_group, group_map)

    group_adj = matrix_to_edges(num_group, group_cost)

    # calculate MST from Graph = (#group, cost)
    return compute_mst(num_group, group_adj)