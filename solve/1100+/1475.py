# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(num):
    """write your logic here"""
    digits = [0] * 10
    while num > 0:
        digits[num % 10] += 1
        num //= 10
    
    count = 0
    for d in range(10):
        if d == 9:
            continue
        elif d == 6:
            count = max(count, (digits[6] + digits[9] + 1) // 2)
        else:
            count = max(count, digits[d])
    
    return count


def test():
    """write your test here"""
    assert solve(9999) == 2
    assert solve(122) == 2
    assert solve(12635) == 1
    assert solve(888888) == 6


def main():
    """write your i/o here"""
    num = input_one(int)
    print(solve(num))


test()
main()
