# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(students):
    """write your logic here"""
    count, alignment = 0, [students[0]]

    for student in students[1:]:
        if alignment[-1] < student:
            alignment.append(student)
        else:
            for i in range(len(alignment)):
                if student < alignment[i]:
                    count += len(alignment) - i
                    alignment.insert(i, student)
                    break

    return count


def test():
    """write your test here"""
    assert 1 == 1


def main():
    """write your i/o here"""
    num_testcase = input_one(int)
    for test_id in range(num_testcase):
        print(test_id + 1, solve(input_list(int)[1:]))


test()
main()
