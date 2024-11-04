# My Solution : https://github.com/ywcheong/solved-baekjoon

# Header
''' import header here '''


import sys
input = lambda: sys.stdin.readline().strip()
input_list = lambda wanted_type: list(map(wanted_type, input().split()))

TESTCASE_ID = 1
def equal(left, right):
    global TESTCASE_ID
    if left == right:
        print(f"Testcase {TESTCASE_ID}: OK ({left} == {right})")
    else:
        print(f"Testcase {TESTCASE_ID}: FAIL ({left} != {right})")
    TESTCASE_ID += 1

# Implementation
''' write code here '''
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a%b)

class Quad:
    def __init__(self, p, q):
        self.p, self.q = p, q
        self.reduce()
    def __str__(self):
        return f"{self.p}/{self.q}"
    def reduce(self):
        gcd = gcd(self.p, self.q)
        self.p, self.q = self.p // gcd, self.q // gcd

def fact(n):
    result = 1
    for x in range(1, n+1):
        result *= x
    return result

def get_prob(target, L):
    pass

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(get_prob(2, [3, 2, 1]), '1/3')
    equal(get_prob(10, [10, 100, 1000, 10000, 100000]), '1/1')
    equal(get_prob(10, [11, 101, 1001, 10001, 100001]), '0/1')
    equal(get_prob(21, [13, 10129414190271203, 102, 102666818896, 1216, 1217, 1218, 101278001, 1000021412678412681]), '5183/36288')

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''

# Case-switch
if __name__ == '__main__':
    test()# submit()