# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys

class Storage:
    def __init__(self):
        self.add = 0
        self.xor = 0

    def push(self, num):
        self.add += num
        self.xor ^= num

    def pop(self, num):
        self.add -= num
        self.xor ^= num

    def get_add(self):
        return self.add
    
    def get_xor(self):
        return self.xor


def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    num_query = input_one(int)

    my_storage = Storage()

    for query_id in range(num_query):
        query_tokens = input_list(int)
        command = query_tokens[0]
        argument = query_tokens[1] if len(query_tokens) == 2 else None

        if command == 1:
            my_storage.push(argument)
        elif command == 2:
            my_storage.pop(argument)
        elif command == 3:
            print(my_storage.get_add())
        elif command == 4:
            print(my_storage.get_xor())
        else:
            raise ValueError("Unknown command")

main()
