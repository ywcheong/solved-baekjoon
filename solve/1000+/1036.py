# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


ORDER_0 = ord("0")
ORDER_A = ord("A")


def digit_to_index(digit):
    if (diff := ord(digit) - ORDER_0) < 10:
        return diff
    return ord(digit) - ORDER_A + 10


def index_to_digit(index):
    if index < 10:
        return chr(index + ORDER_0)
    return chr(index - 10 + ORDER_A)


def value_to_number(value):
    if value == 0:
        return "0"

    result = []

    while value > 0:
        result.append(index_to_digit(value % 36))
        value //= 36

    return "".join(reversed(result))


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(numbers, k):
    """write your logic here"""
    result = 0
    digit_strengths = [0] * 36

    for number in numbers:
        for shift, digit in enumerate(reversed(number)):
            index = digit_to_index(digit)
            digit_strengths[index] += (35 - index) * (36**shift)
            result += index * (36**shift)

    digit_strengths.sort(reverse=True)
    for strength in digit_strengths[:k]:
        result += strength

    return value_to_number(result)


def test():
    """write your test here"""
    assert 1 == 1


def main():
    """write your i/o here"""
    size = input_one(int)
    numbers = [None] * size
    for i in range(size):
        numbers[i] = input_one(str)
    k = input_one(int)
    print(solve(numbers, k))


test()
main()
