# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys, gc


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def main():
    """write your code here"""
    num_color, num_nick = input_list(int)
    color_set, nick_set = set(), set()

    for _ in range(num_color):
        color_set.add((input_one(str)))

    for _ in range(num_nick):
        nick_set.add(input_one(str))

    num_team = input_one(int)
    for _ in range(num_team):
        team = input_one(str)
        is_break = False

        # 핵심 최적화: team 문자열을 아무렇게나 쪼개는 것이 아니라 문제에서 주어진 조건대로
        #           양 조각의 길이가 1000 이하가 되도록 유지하면서 자르는 시작, 끝 찾기
        spos_start, spos_end = None, None
        if len(team) <= 1001:
            spos_start, spos_end = 1, len(team)
        else:
            spos_start, spos_end = len(team) - 1000, 1001

        # team 문자열을 두 조각으로 나눈 뒤 각각의 set에 대해서 검사 실시
        for spos in range(spos_start, spos_end):
            if team[:spos] in color_set and team[spos:] in nick_set:
                print("Yes")
                is_break = True
                break

        if not is_break:
            print("No")


main()

# 참고로, 이 문제에서 팀 이름으로 사용 가능한 모든 문자열을 생성하고
# 푸는 식으로 진행할 경우 시간 복잡도에 걸림
