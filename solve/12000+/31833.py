# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def until_green(timer, green, red):
    timer %= green + red
    # 0, 1, ..., g-1, g, g+1, ..., g+r-1
    # <-- [ ok ] --> | <-- [  no   ] -->
    if timer < green:
        return 0
    return (green + red) - timer


def solve(crossing_times, bridge_times, greens, reds):
    """write your logic here"""
    num_section = len(crossing_times)
    assert num_section == len(bridge_times) == len(greens) == len(reds)

    timer = 0
    for i in range(num_section):
        crossing_elapse = until_green(timer, greens[i], reds[i]) + crossing_times[i]
        bridge_elapse = bridge_times[i]
        timer += min(crossing_elapse, bridge_elapse)

    return timer


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(1 + 1, 2)


def main():
    """write your i/o here"""
    num_section = input_one(int)
    crossing_times, bridge_times, greens, reds = (
        [None] * num_section,
        [None] * num_section,
        [None] * num_section,
        [None] * num_section,
    )

    for i in range(num_section):
        crossing_times[i], bridge_times[i], greens[i], reds[i] = input_list(int)

    print(solve(crossing_times, bridge_times, greens, reds))


# test()
main()
