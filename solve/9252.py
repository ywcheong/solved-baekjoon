# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys

sys.setrecursionlimit(3000)


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    p, q = input_one(str), input_one(str)
    # p, q = "ABBAA" * 200, "AB" * 500
    memo = dict()

    def solve(p_end, q_end):
        if p_end == 0 or q_end == 0:
            return 0
        if (p_end, q_end) in memo:
            return memo[p_end, q_end]

        result = None

        if p[p_end - 1] == q[q_end - 1]:
            result = solve(p_end - 1, q_end - 1) + 1
        else:
            result = max(
                solve(p_end - 1, q_end),
                solve(p_end, q_end - 1),
            )

        memo[p_end, q_end] = result
        return result

    answer_length = solve(len(p), len(q))
    print(answer_length)

    if answer_length == 0:
        return

    pdx, qdx = len(p), len(q)
    answer_seq = []
    while pdx > 0 and qdx > 0:
        if p[pdx - 1] == q[qdx - 1]:
            answer_seq.append(p[pdx - 1])
            pdx -= 1
            qdx -= 1
        else:
            if memo.get((pdx - 1, qdx), 0) > memo.get((pdx, qdx - 1), 0):
                pdx -= 1
            else:
                qdx -= 1
    print("".join(reversed(answer_seq)))


main()
