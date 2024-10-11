# Implementation
def get_count(n):
    MEMO = [x - 1 for x in range(n+1)]

    for x in range(2, n+1):
        # Case 1
        if x % 3 == 0:
            MEMO[x] = min(MEMO[x], MEMO[x//3] + 1)

        # Case 2
        if x % 2 == 0:
            MEMO[x] = min(MEMO[x], MEMO[x//2] + 1)

        # Case 3
        MEMO[x] = min(MEMO[x], MEMO[x-1] + 1)

    return MEMO[n]

# Testing
def test():
    print("WARNING: TEST MODE")

    assert get_count(1) == 0
    assert get_count(2) == 1
    assert get_count(10) == 3
    assert get_count(1000000) < 1000000

    print("TEST DONE")

# Submit
def submit():
    n = int(input())
    print(get_count(n))

# Case-switch
if __name__ == '__main__':
    submit()