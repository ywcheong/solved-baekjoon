# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


OPERATOR_ORDER = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}


def tokenizer(raw_string: str):
    return list(raw_string)


def is_identifier(token):
    return token not in OPERATOR_ORDER and token not in ['(', ')']


def shunting_yard(token_list):
    output, operator_stack = [], []

    for token in token_list:
        # Identifier -> Output 직행
        if is_identifier(token):
            output.append(token)

        # Left Parenthesis: 삽입
        elif token == "(":
            operator_stack.append(token)

        # Right Parenthesis: Match 찾을때까지 헤집기
        elif token == ")":
            while operator_stack and operator_stack[-1] != "(":
                output.append(operator_stack.pop())
            operator_stack.pop()  # ( 삭제

        # 일반 연산자:
        else:
            while (
                operator_stack  # 비면 중단
                and operator_stack[-1] != '('   # 열린괄호면 중단
                and OPERATOR_ORDER[operator_stack[-1]] >= OPERATOR_ORDER[token] # 하순위만 남으면 중단
            ):
                output.append(operator_stack.pop())
            operator_stack.append(token)

        # print(f"token = {token}\nopstak = {operator_stack}\noutput = {output}\n\n")

    # 끝나면 한번에 처리
    while operator_stack:
        output.append(operator_stack.pop())

    return "".join(output)


def main():
    """write your code here"""
    print(shunting_yard(tokenizer(input_one(str))))


main()
