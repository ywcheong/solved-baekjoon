# Implementation
class User:
    def __init__(self, age, name, order):
        self.age = age
        self.name = name
        self.order = order

    def __lt__(self, s):
        # <-> (self < s)
        if self.age != s.age:
            return self.age < s.age
        
        return self.order < s.order
    
    def __str__(self):
        return f"{self.age} {self.name}"


# Testing
def test():
    print("WARNING: TEST MODE")

    user_list = [
        User(21, 'Junkyu', 0),
        User(21, 'Dohyun', 1),
        User(20, 'Sunyoung', 2),
    ]

    assert sorted(user_list) == [user_list[2], user_list[0], user_list[1]]

    print("TEST DONE")

# Submit
def submit():
    import sys

    n = int(input())
    user_list = [None] * n

    for i in range(n):
        age, name = sys.stdin.readline().strip().split()
        user_list[i] = User(int(age), name, i)

    for user in sorted(user_list):
        print(str(user))

# Case-switch
if __name__ == '__main__':
    submit()