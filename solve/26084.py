# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(a):
    """write your logic here"""
    return None


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(1 + 1, 2)


def perm(n, k):
    if k == 1:
        return n
    elif k == 2:
        return n * (n - 1) // 2
    elif k == 3:
        return n * (n - 1) * (n - 2) // 6


def main():
    """write your i/o here"""
    team = input_one(str)
    teams = dict()
    for char in team:
        teams[char] = teams.get(char, 0) + 1

    num_user = input_one(int)
    users = dict()
    for _ in range(num_user):
        first_letter = input_one(str)[0]
        users[first_letter] = users.get(first_letter, 0) + 1

    # print(teams, users)

    result = 1
    for char in teams:
        team_size = teams.get(char, 0)
        user_size = users.get(char, 0)

        if team_size > user_size:
            result = 0
        result *= perm(user_size, team_size)
    print(result)
        

main()
