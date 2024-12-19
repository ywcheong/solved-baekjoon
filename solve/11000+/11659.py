# Header
import sys
input = lambda: sys.stdin.readline().strip()
input_list = lambda wanted_type: list(map(wanted_type, input().split()))

# Implementation
''' write code here '''
def get_partial_sum(L):
    # S[i] = S[0] + ... + L[i]
    S = [None] * len(L)
    S[0] = L[0]

    for i in range(1, len(L)):
        S[i] = S[i-1] + L[i]

    return S

def get_range_sum(S, a, b):
    # L[a] + ... L[b]
    # if a == 0: S[b]
    # else: S[b] - S[a-1]
    a, b = a-1, b-1
    if a == 0:
        return S[b]
    else:
        return S[b] - S[a-1]

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    L = [5,4,3,2,1]
    S = get_partial_sum(L)
    assert S == [5, 9, 12, 14, 15]
    assert get_range_sum(S, 1, 3) == 12
    assert get_range_sum(S, 2, 4) == 9
    assert get_range_sum(S, 5, 5) == 1

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    import sys
    _, cases = input_list(int)
    L = input_list(int)
    S = get_partial_sum(L)

    for _ in range(cases):
        a, b = input_list(int)
        print(get_range_sum(S, a, b))

# Case-switch
if __name__ == '__main__':
    submit()