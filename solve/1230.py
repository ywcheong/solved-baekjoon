# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline()[:-1])


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(original, target):
    """write your logic here"""
    olen, tlen = len(original), len(target)
    memo = [[None] * (tlen + 1) for _ in range(olen + 1)]

    for o_sublen in range(olen + 1):
        for t_sublen in range(tlen + 1):
            result = None

            if o_sublen == 0:
                if t_sublen == 0:
                    result = 0
                else:
                    result = 1
            else:
                o_char = original[o_sublen - 1]
                result = float("inf")

                for t_index in range(t_sublen):
                    t_char = target[t_index]

                    if o_char == t_char:
                        this_result = memo[o_sublen - 1][t_index]

                        if t_index < t_sublen - 1:
                            this_result += 1

                        result = min(result, this_result)

            memo[o_sublen][t_sublen] = result

    output = memo[olen][tlen]
    if output == float("inf"):
        return -1
    return output


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(solve("hello fine", "hello, how are you? I'm fine thank you and you?"), 2)
    check(solve("aaaaa", "ababababa"), 4)
    check(solve("no way", "No way!"), -1)
    check(solve("abcefijklmnopuvwxz", "abcdefghijklmnopqrstuvwxyz"), 4)
    check(solve("B", "ABC"), 2)
    check(solve("A", "ABC"), 1)
    check(solve("C", "ABC"), 1)
    check(solve("C", "ABCDE"), 2)
    check(solve("", ""), 0)
    check(solve("A", ""), -1)
    check(solve("", "A"), 1)


def main():
    """write your i/o here"""
    original = input_one(str)
    target = input_one(str)
    print(solve(original, target))


# test()
main()
