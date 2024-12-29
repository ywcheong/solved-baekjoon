# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys

START, END, JUMP = 0, 1, 2


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """ 입출력 코드 """
    num_chest, num_rule, num_nut = input_list(int)
    rules = [None] * num_rule
    for i in range(num_rule):
        rules[i] = input_list(int)

    """ 문제풀이 코드 """
    
    def compute_nut(start, end, jump):
        """ 도토리는 주어진 start, end, jump 규칙에서, 총 몇 개인가? """
        if end < start:
            return 0
        return (end - start) // jump + 1

    def compute_batch_nuts(global_end):
        """ 도토리 개수를 ~global_end까지만 계산한다면, 총 몇 개인가? """
        count = 0
        for start, end, jump in rules:
            count += compute_nut(start, min(end, global_end), jump)
        return count

    def cond(mid):
        """ Parametric Search를 위한 보조 함수: ~mid까지의 도토리 합이 원하는 만큼인가? """
        return compute_batch_nuts(mid) >= num_nut

    def parametric_search(lo, hi):
        """ Parametric Search 구현 """
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if cond(mid):  # X O O
                hi = mid
            else:
                lo = mid
        return hi

    """ 0번까지만 세면 될 리가 없음 && num_chest까지 세면 무조건 됨 """
    print(parametric_search(0, num_chest))


main()
