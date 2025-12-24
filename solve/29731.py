# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


RICKROLL = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop",
]


def main():
    """write your code here"""
    size = input_one(int)
    for _ in range(size):
        given_text = input_one(str)
        if all((given_text not in rick) for rick in RICKROLL):
            print("Yes")
            return
    print("No")


main()
