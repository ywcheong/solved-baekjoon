# Implementation
MEMO = dict()

def add_count(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])


def get_count(n):
    if n == 0:
        return (1, 0)
    if n == 1:
        return (0, 1)
    if n in MEMO:
        return MEMO[n]
    
    MEMO[n] = add_count(get_count(n-1), get_count(n-2))
    return MEMO[n]


# Testing
def test():
    print("WARNING: TEST MODE")

    assert get_count(0) == (1, 0)
    MEMO = dict()

    assert get_count(1) == (0, 1)
    MEMO = dict()
    
    assert get_count(3) == (1, 2)
    MEMO = dict()
    
    assert get_count(6) == (5, 8)
    MEMO = dict()
    
    assert get_count(22) == (10946, 17711)
    MEMO = dict()

    print("TEST DONE")


# Submit
def submit():
    n = int(input())
    for _ in range(n):
        result = get_count(int(input()))
        print(f"{result[0]} {result[1]}")

# Case-switch
if __name__ == "__main__":
    submit()
