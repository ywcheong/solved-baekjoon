# Implementation
def get_case(n):
    MEMO = dict()
    MEMO[1], MEMO[2], MEMO[3] = 1, 2, 4

    for x in range(4, n+1):
        MEMO[x] = MEMO[x-1] + MEMO[x-2] + MEMO[x-3]

    return MEMO[n]

# Testing
def test():
    print("WARNING: TEST MODE")

    assert get_case(1) == 1
    assert get_case(2) == 2
    assert get_case(4) == 7
    assert get_case(7) == 44
    assert get_case(10) == 274

    print("TEST DONE")

# Submit
def submit():
    n = int(input())

    for _ in range(n):
        print(get_case(int(input())))

# Case-switch
if __name__ == '__main__':
    submit()