# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    for _ in range(15):
        image_row = input_list(str)
        if "w" in image_row:
            print("chunbae")
            return
        elif "b" in image_row:
            print("nabi")
            return
        elif "g" in image_row:
            print("yeongcheol")
            return

    raise ValueError("No cat found")


main()
