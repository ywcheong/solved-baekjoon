# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def get_push_index(array, push):
    # 1 3 5 7 8 << 6?
    #       ^ ^
    # 1 3 5 7 8 << 7?
    #       ^ ^
    def cond(mid):
        return push <= array[mid]

    lo, hi = -1, len(array)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if cond(mid):
            hi = mid
        else:
            lo = mid
    return hi


def solve(nums):
    """write your logic here"""
    size = len(nums)
    lis_lengths = [1] * size
    lis_counts = [0] * size

    lis_lengths[-1], lis_counts[-1] = 1, 1
    for start in range(size - 2, -1, -1):
        # get lis length, starting from every index
        for next in range(start + 1, size):
            if nums[start] < nums[next]:
                lis_lengths[start] = max(lis_lengths[start], lis_lengths[next] + 1)

        # compute counts which can make lis from every index
        for next in range(start + 1, size):
            if lis_lengths[start] == lis_lengths[next] + 1:
                lis_counts[start] += lis_counts[next]

    max_lis_length = max(lis_lengths)
    return max_lis_length


def test():
    """write your test here"""
    assert 1 == 1


def main():
    """write your i/o here"""
    size = input_one(int)
    nums = input_list(int)
    assert len(nums) == size

    print(solve(nums))


test()
main()
