# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(L):
    """write your code here"""
    lis = [L[0]]
    lislen = [None] * len(L)

    def parametric_search(x, lo, hi):
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if lis[mid] >= x:  # X O O
                hi = mid
            else:  # X X O
                lo = mid
        return hi

    for i, x in enumerate(L):
        # LIS 확장
        if lis[-1] < x:
            lis.append(x)
            lislen[i] = len(lis)
        else:
            push_index = parametric_search(x, -1, len(lis))
            lis[push_index] = x
            lislen[i] = push_index + 1

    print(lis)
    print(lislen)

    # 이때 반드시 역순으로 구해야 한다. 왜냐하면 정순에서는 LIS 삽입 당시의 대소성은
    # 이미 parametric search 과정에서 훼손되었기 때문이다.
    # 하지만 역순에서는 LIS 삽입 당시의 대소성이 보존되어 있다.
    # 예를 들어, [1, 100, 2, 3]을 생각하면 된다.
    # 1 -> 100 -> 3 순서는 보장되지 않으나, 3 -> 2 -> 1은 보장된다.
    result, current_lislen, pos = [], len(lis), len(L) - 1
    while current_lislen > 0:
        if lislen[pos] == current_lislen:
            result.append(L[pos])
            current_lislen -= 1
        pos -= 1

    result.reverse()

    print(len(result))
    print(" ".join(map(str, result)))


def test():
    print([1], ">>")
    solve([1])
    print([1, 2], ">>")
    solve([1, 2])
    print([2, 1], ">>")
    solve([2, 1])
    print([1, 2, 3], ">>")
    solve([1, 2, 3])
    print([1, 3, 2], ">>")
    solve([1, 3, 2])
    print([2, 1, 3], ">>")
    solve([2, 1, 3])
    print([2, 3, 1], ">>")
    solve([2, 3, 1])
    print([3, 1, 2], ">>")
    solve([3, 1, 2])
    print([3, 2, 1], ">>")
    solve([3, 2, 1])
    print([2, 3, 1, 4], ">>")
    solve([2, 3, 1, 4])
    print([10, 30, 50, 70, 10, 30, 50, 70], ">>")


def main():
    _, L = input_one(int), input_list(int)
    solve(L)


main()
