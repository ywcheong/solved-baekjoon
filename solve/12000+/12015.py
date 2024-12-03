# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def test():
    assert 1 == main([60, 50, 40, 30, 20, 10])
    assert 6 == main([10, 20, 30, 40, 50, 60])

    assert main([10]) == 1
    assert main([10, 10]) == 1
    assert main([10, 20]) == 2
    assert main([20, 10]) == 1
    assert main([10, 10, 10]) == 1
    assert main([10, 10, 20]) == 2
    assert main([10, 20, 10]) == 2
    assert main([20, 10, 10]) == 1
    assert main([10, 20, 20]) == 2
    assert main([20, 20, 10]) == 1
    assert main([20, 10, 20]) == 2
    assert main([20, 10, 30]) == 2
    assert main([30, 10, 20]) == 2
    assert main([10, 20, 30]) == 3


def main(L):
    """write your code here"""
    size = len(L)

    lis = [float("-inf")] * size

    lis[0] = L[0]
    lis_length = 1

    for i in range(1, size):
        # try to put x in LIS...
        x = L[i]

        # if x is the biggest:
        if lis[lis_length - 1] < x:
            lis[lis_length] = x
            lis_length = lis_length + 1
            continue

        # if x is NOT the biggest...
        # find place to insert x
        # 10 20 30
        #    ^ Insertable: 11~20

        # x-1  x   x+1
        # X    O   O

        def cond(mid):
            return x <= lis[mid]

        lo, hi = -1, lis_length - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if cond(mid):  # X O O
                hi = mid
            else:
                lo = mid
        lis[hi] = x
    
    return lis_length


test()
_ = input_one(int)
L = input_list(int)
print(main(L))
