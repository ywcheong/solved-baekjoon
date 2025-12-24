# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(switches, students):
    """write your logic here"""
    result = switches[:]
    num_switch = len(switches)

    def toggle(id):
        # print(f"Toggle Go Sw{id} -> {switches[id-1]}")
        result[id - 1] = 1 - result[id - 1]

    for sex, given_num in students:
        # print(f"GivenSex {sex} givenNum {given_num}")
        if sex == MALE:
            pos = given_num
            while pos <= num_switch:
                toggle(pos)
                pos += given_num
        elif sex == FEMALE:
            toggle(given_num)
            pos_left, pos_right = given_num - 1, given_num + 1
            while 1 <= pos_left and pos_right <= num_switch and result[pos_left-1] == result[pos_right-1]:
                toggle(pos_left)
                toggle(pos_right)
                pos_left -= 1
                pos_right += 1
        else:
            raise ValueError("Wrong sex")
        
    return result


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(solve([0, 1, 0, 1, 0, 0, 0, 1], [[1, 3], [2, 3]]), [1, 0, 0, 0, 1, 1, 0, 1])


MALE, FEMALE = 1, 2

def main():
    """write your i/o here"""
    num_switch = input_one(int)
    switches = input_list(int)

    num_student = input_one(int)
    students = [None] * num_student
    for i in range(num_student):
        students[i] = input_list(int)
    
    result = solve(switches, students)
    
    for i, x in enumerate(result):
        if (i + 1) % 20 == 0:
            print(x)
        else:
            print(x, end=" ")


# test()
main()
