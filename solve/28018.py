# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys

MAX_TIME = 1_000_001

def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(segments, queries):
    """write your logic here"""
    num_query = len(queries)

    events = [0] * MAX_TIME
    for alloc_time, free_time in segments:
        events[alloc_time] += 1
        if free_time + 1 < MAX_TIME:
            events[free_time + 1] -= 1

    # times[t] : t초의 점유중 좌석수
    # times[t] := times[t-1] + alloc_event[t] - free_event[t-1]
    times = [None] * MAX_TIME
    times[0] = 0
    for i in range(1, MAX_TIME):
        times[i] = times[i - 1] + events[i]

    result = [None] * num_query
    for i, q in enumerate(queries):
        if 0 <= q < MAX_TIME:
            result[i] = times[q]
        else:
            result[i] = 0

    return result



def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(solve([[1, 3]], [2, 4]), [1, 0])
    check(solve([[1, 5], [3, 6]], [2, 3, 7]), [1, 2, 0])


def main():
    """write your i/o here"""
    num_segment = input_one(int)
    segments = [None] * num_segment
    for i in range(num_segment):
        segments[i] = input_list(int)

    _num_query = input_one(int)
    queries = input_list(int)
    assert _num_query == len(queries)
    
    print("\n".join(map(str, solve(segments, queries))))


# test()
main()
