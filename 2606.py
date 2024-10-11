from collections import deque

# Implementation
""" write code here """
def get_dict_edge(node, edge):
    result = dict()

    for v in node:
        result[v] = set()

    for (v, w) in edge:
        result[v] |= {w}
        result[w] |= {v}
    
    return result

def get_count(node, edge):
    starting = [1]
    to_visit, checked = deque(starting), set(starting)
    result = []

    while len(to_visit) > 0:
        # Current Node
        v = to_visit.popleft() # BFS (.pop for DFS)

        # Find next Node
        for w in edge[v]:
            if w not in checked:
                # Mark as checked
                to_visit.append(w)
                checked.add(w)

    return len(checked - {1})


# Testing
def test():
    print("WARNING: TEST MODE")

    node = list(range(1, 8))
    edge = [(1, 2), (2, 3), (1, 5), (5, 2), (5, 6), (4, 7)]

    edge = get_dict_edge(node, edge)

    assert get_count(node, edge) == 4

    print("TEST DONE")


# Submit
def submit():
    node = list(range(1, 1 + int(input())))
    edge = [None] * int(input())

    for i in range(len(edge)):
        v, w = map(int, input().split())
        edge[i] = (v, w)
    
    print(get_count(node, get_dict_edge(node, edge)))


# Case-switch
if __name__ == "__main__":
    submit()
