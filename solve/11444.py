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
divisor = 1000000007

def multiply_matrix(A, B):
    a0, a1 = A
    a00, a01 = a0
    a10, a11 = a1

    b0, b1 = B
    b00, b01 = b0
    b10, b11 = b1

    return (
        ((a00*b00+a01*b10)%divisor, (a00*b01+a01*b11)%divisor),
        ((a10*b00+a11*b10)%divisor, (a10*b01+a11*b11)%divisor)
    )

def power_matrix(A, n):
    if n == 0:
        return ((1, 0), (0, 1))
    elif n == 1:
        return A
    elif n % 2 == 0:
        half_matrix = power_matrix(A, n//2)
        return multiply_matrix(half_matrix, half_matrix)
    else:
        half_matrix = power_matrix(A, n//2)
        return multiply_matrix(multiply_matrix(half_matrix, half_matrix), A)
    
def get_fibonacci(n):
    fibonacci_matrix = ((1, 1), (1, 0))
    return power_matrix(fibonacci_matrix, n)[1][0] % divisor

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(get_fibonacci(1000), 517691607)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    n = int(input())
    print(get_fibonacci(n))

# Case-switch
if __name__ == '__main__':
    submit()