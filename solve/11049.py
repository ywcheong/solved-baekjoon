# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(matrix_size, start, end, memo):
    if start == end:
        return 0
    elif start + 1 == end:
        return matrix_size[start] * matrix_size[start + 1] * matrix_size[start + 2]
    elif (start, end) in memo:
        return memo[start, end]

    result = float("inf")

    memo[start, end] = result
    return result


def main():
    matrix_count = input_one(int)
    matrix_size = [None] * (matrix_count + 1)
    for i in range(matrix_count):
        # 비효율적인데 500번이라 그냥넘어감
        matrix_size[i], matrix_size[i + 1] = input_list(int)

    memo = [[None] * matrix_count for _ in range(matrix_count)]
    for length in range(1, matrix_count + 1):
        for start in range(matrix_count - length + 1):
            end = start + (length - 1)
            if length == 1:
                memo[start][end] = 0
            elif length == 2:
                memo[start][end] = (
                    matrix_size[start] * matrix_size[start + 1] * matrix_size[start + 2]
                )
            else:
                result = float("inf")
                for mid in range(start, end):
                    result = min(
                        result,
                        memo[start][mid]
                        + memo[mid + 1][end]
                        + matrix_size[start]
                        * matrix_size[end + 1]
                        * matrix_size[mid + 1],
                    )
                memo[start][end] = result

            # print(f"{start} ~ {end} // {memo[start][end]}")

    print(memo[0][-1])


main()
