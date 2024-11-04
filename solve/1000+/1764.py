# Implementation
def intersection(A, B):
    return sorted(list(set(A) & set(B)))

# Testing
def test():
    print("WARNING: TEST MODE")

    A = ['ohhenrie', 'charlie', 'baesangwook']
    B = ['obama', 'baesangwook', 'ohhenrie', 'clinton']

    assert intersection(A, B) == ['baesangwook', 'ohhenrie']

    print("TEST DONE")

# Submit
def submit():
    import sys
    n, m = list(map(int, input().split()))
    A, B = [None] * n, [None] * m

    for i in range(n):
        A[i] = sys.stdin.readline().strip()
    for i in range(m):
        B[i] = sys.stdin.readline().strip()
    
    result = intersection(A, B)
    print(len(result))
    print("\n".join(result))

# Case-switch
if __name__ == '__main__':
    submit()