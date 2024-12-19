# Header
import sys
input = lambda: sys.stdin.readline().strip()
input_list = lambda wanted_type: list(map(wanted_type, input().split()))

# Implementation
''' write code here '''
def get_case(n):
    MEMO = dict()
    MEMO[1], MEMO[2] = 1, 2

    for x in range(3, n + 1):
        MEMO[x] = (MEMO[x-1] + MEMO[x-2]) % 10007

    return MEMO[n]

# Testing
def test():
    print("WARNING: TEST MODE")

    assert get_case(2) == 2
    assert get_case(9) == 55

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    n = int(input())
    print(get_case(n))

# Case-switch
if __name__ == '__main__':
    submit()