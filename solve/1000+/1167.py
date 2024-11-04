#############################################
#     THIS SOLUTION IS BASED ON 1967.py     #
#############################################

# My Solution : https://github.com/ywcheong/solved-baekjoon

# Header
""" import header here """
import sys

input = lambda: sys.stdin.readline().strip()
input_list = lambda wanted_type: list(map(wanted_type, input().split()))

TESTCASE_ID = 1


def equal(left, right):
    global TESTCASE_ID
    if left == right:
        print(f"Testcase {TESTCASE_ID}: OK ({left} == {right})")
    else:
        print(f"Testcase {TESTCASE_ID}: FAIL ({left} != {right})")
    TESTCASE_ID += 1


# Implementation
""" write code here """
sys.setrecursionlimit(100500)

def get_child_map(edge):
    child_map = dict()
    for parent, child, weight in edge:
        if parent not in child_map:
            child_map[parent] = [(weight, child)]
        else:
            child_map[parent].append((weight, child))
    return child_map


def solve_diameter(edge):
    child_map = get_child_map(edge)

    def solve(node):
        this_depth, this_diameter = 0, 0

        if node not in child_map:
            return this_depth, this_diameter
        
        child_depth_list, child_diameter_list = [], []
        for child_weight, child_node in child_map[node]:
            child_depth, child_diameter = solve(child_node)
            child_depth_list.append(child_depth + child_weight)
            child_diameter_list.append(child_diameter)
        
        this_depth = max(child_depth_list)
        
        if len(child_map[node]) == 1:
            child_depth_list.sort()
            diameter_containing_this = child_depth_list[-1]
            child_diameter_list.append(diameter_containing_this)
            this_diameter = max(child_diameter_list)
        else:
            child_depth_list.sort()
            diameter_containing_this = child_depth_list[-1] + child_depth_list[-2]
            child_diameter_list.append(diameter_containing_this)
            this_diameter = max(child_diameter_list)
    
        return this_depth, this_diameter

    root_depth, root_diameter = solve(1)
    return root_diameter


# Testing
def test():
    print("WARNING: TEST MODE")

    """ test here """
    # equal(1, 1) -> OK (1 == 1)
    # equal(2, 1) -> FAIL (2 == 1)
    equal(
        solve_diameter(
            [
                (1, 2, 3),
                (1, 3, 2),
                (2, 4, 5),
                (3, 5, 11),
                (3, 6, 9),
                (4, 7, 1),
                (4, 8, 7),
                (5, 9, 15),
                (5, 10, 4),
                (6, 11, 6),
                (6, 12, 10),
            ]
        ),
        45,
    )

    equal(
        solve_diameter(
            [
                (1, 2, 3),
                (1, 3, 2),
                (3, 4, 7),
                (3, 5, 11),
            ]
        ),
        18,
    )

    equal(
        solve_diameter(
            [
                (1, 2, 20),
                (1, 3, 2),
                (3, 4, 7),
                (3, 5, 11),
            ]
        ),
        33
    )

    print("TEST DONE")


# Submit
def submit():
    """get input here"""
    node_count = int(input())
    edge = []
    for _ in range(node_count):
        line = input_list(int)
        start = line[0]
        end_list, weight_list = line[1:-1:2], line[2:-1:2]
        for end, weight in zip(end_list, weight_list):
            if end < start:
                continue
            edge.append((start, end, weight))
    print(solve_diameter(edge))

# Case-switch
if __name__ == "__main__":
    # test()
    submit()