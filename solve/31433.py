# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys

NEXT_CHAR = {"K": "S", "S": "A", "A": "K"}

def solve(text):
    """write your solution here"""
    size = len(text)
    klen, kpos = 0, "K"
    slen, spos = 0, "S"
    alen, apos = 0, "A"

    for char in text:
        if char == kpos:
            klen, kpos = klen + 1, NEXT_CHAR[kpos]
        if char == spos:
            slen, spos = slen + 1, NEXT_CHAR[spos]
        if char == apos:
            alen, apos = alen + 1, NEXT_CHAR[apos]

    return 2 * min(
        size - klen,
        max(1, size - slen),
        max(2, size - alen),
    )


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve("KKSKASKA"), 8)
    check(solve("KSAKSAKSA"), 0)
    check(solve("SAKSAKSAK"), 2)
    check(solve("SAKSAKSAA"), 2)
    check(solve("AKSAKSAKS"), 2)
    check(solve("AKSAKSAKK"), 4)
    check(solve("AKSAKSKKK"), 6)
    check(solve("KKSAKSKKK"), 8)
    check(solve("KKKKK"), 8)
    check(solve("SSSSS"), 8)
    check(solve("AAAAA"), 8)
    check(solve("KAKSAKSAKAKK"), 8)


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    text = input_one(str)
    print(solve(text))


# test()
main()
