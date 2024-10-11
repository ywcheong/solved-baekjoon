# Implementation
def comb(n, k):
    return fact(n) // fact(k) // fact(n-k)

def fact(n):
    result = 1
    for x in range(1, n+1):
        result *= x
    return result

# Testing
def test():
    print("WARNING: TEST MODE")

    assert comb(5, 5) == 1
    assert comb(5, 4) == 5
    assert comb(5, 3) == 10
    assert comb(5, 2) == 10
    assert comb(5, 1) == 5
    assert comb(5, 0) == 1

    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(2) == 2
    assert fact(3) == 6

    print("TEST DONE")

# Submit
def submit():
    n, k = list(map(int, input().split()))
    print(comb(n, k))

# Case-switch
if __name__ == '__main__':
    submit()