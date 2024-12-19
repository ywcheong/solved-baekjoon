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


def get_batch_sum(pos_list, partial_sum):
    return [
        get_sum(start_pos, end_pos, partial_sum)
        for start_pos, end_pos in pos_list
    ]


def get_sum(start_pos, end_pos, partial_sum):
    # 1을 빼는 것은 1-index에서 0-index로의 변화를 위해서이며,
    # sx, sy에서 1을 더 빼는 것은 좌표를 left-top으로 1칸 이동시켜
    # 포함-배제의 경계를 만들기 위해서이다.
    sx, sy = start_pos[0] - 2, start_pos[1] - 2
    ex, ey = end_pos[0] - 1, end_pos[1] - 1

    # 포함-배제의 원리
    return (
        calculate_partial(partial_sum, ex, ey)
        - calculate_partial(partial_sum, sx, ey)
        - calculate_partial(partial_sum, ex, sy)
        + calculate_partial(partial_sum, sx, sy)
    )


def calculate_partial(partial_sum, row, column):
    if row < 0 or column < 0:
        return 0
    return partial_sum[row][column]


def make_partial_sum(nums):
    # (0, 0) ~ (end_pos)
    N = len(nums)
    partial_sum = [[None] * N for _ in range(N)]

    for row in range(N):
        for column in range(N):
            partial_sum[row][column] = (
                nums[row][column]
                + calculate_partial(partial_sum, row - 1, column)
                + calculate_partial(partial_sum, row, column - 1)
                - calculate_partial(partial_sum, row - 1, column - 1)
            )

    return partial_sum


# Testing
def test():
    print("WARNING: TEST MODE")

    """ test here """
    # equal(1, 1) ->
    partial_1 = make_partial_sum(
        [
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6],
            [4, 5, 6, 7],
        ]
    )

    equal(get_batch_sum([
        [(2, 2), (3, 4)],
        [(3, 4), (3, 4)],
        [(1, 1), (4, 4)],
    ], partial_1), [27, 6, 64])

    partial_2 = make_partial_sum(
        [
            [1, 2],
            [3, 4],
        ]
    )

    equal(get_batch_sum([
        [(1, 1), (1, 1)],
        [(1, 2), (1, 2)],
        [(2, 1), (2, 1)],
        [(2, 2), (2, 2)],
    ], partial_2), [1, 2, 3, 4])

    print("TEST DONE")


# Submit
def submit():
    """get input here"""
    size, cases = input_list(int)
    nums = [None] * size
    pos_list = [None] * cases

    for i in range(size):
        nums[i] = input_list(int)

    for i in range(cases):
        sx, sy, ex, ey = input_list(int)
        pos_list[i] = [(sx, sy), (ex, ey)]
    
    partial_sum = make_partial_sum(nums)
    sum_list = get_batch_sum(pos_list, partial_sum)

    print("\n".join(map(str, sum_list)))

# Case-switch
if __name__ == "__main__":
    submit()
