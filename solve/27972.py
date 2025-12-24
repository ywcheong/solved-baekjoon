# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def solve(notes):
    """write your solution here"""
    size = len(notes)

    answer = 1
    decrease_stack, increase_stack = 1, 1

    for i in range(size - 1):
        this, next = notes[i], notes[i + 1]
        if this < next:
            increase_stack += 1
            decrease_stack = 1
        if this > next:
            increase_stack = 1
            decrease_stack += 1
        
        answer = max(answer, increase_stack, decrease_stack)

    return answer


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve([3, 1, 5, 4, 2]), 3)
    check(solve([3, 1, 1, 2, 1, 3]), 2)
    check(solve([5, 4, 3, 2, 1]), 5)
    check(solve([1, 2, 3, 4, 5, 4, 3, 2, 1]), 5)


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    size = input_one(int)
    notes = input_list(int)
    print(solve(notes))


# test()
main()
