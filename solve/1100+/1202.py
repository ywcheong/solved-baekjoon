# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import namedtuple
from typing import List

Jewel = namedtuple('Jewel', ['weight', 'price'])

def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    num_jewels, num_bags = input_list(int)
    
    jewel_list: List[Jewel] = [None] * num_jewels
    for i in range(num_jewels):
        weight, price = input_list(int)
        jewel_list[i] = Jewel(weight=weight, price=price)

    jewel_list.sort(key=lambda jw: jw.price, reverse=True)
    
    bag_list: List[int] = [None]* num_bags
    for i in range(num_bags):
        bag_list[i] = input_one(int)

    bag_list.sort()

    price_sum = 0
    for jewel in jewel_list:
        weight, price = jewel.weight, jewel.price
        if 

    return price_sum


main()
