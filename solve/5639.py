# My Solution : https://github.com/ywcheong/solved-baekjoon

# Header
''' import header here '''


import sys
sys.setrecursionlimit(100000)
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
def get_order(NLR):
    length = len(NLR)
    LNR = sorted(NLR)
    LNR_quickpos = dict()
    for i, x in enumerate(LNR):
        LNR_quickpos[x] = i
    return get_LRN(NLR, 0, length, LNR, 0, length, LNR_quickpos)

def get_LRN(NLR, NLR_start, NLR_end, LNR, LNR_start, LNR_end, LNR_quickpos):
    # NLR = N + NLR(left) + NLR(right)
    # LNR = LNR(left) + N + LNR(right)
    assert NLR_start <= NLR_end
    assert LNR_start <= LNR_end
    assert LNR_end - LNR_start == NLR_end - NLR_start
    length = NLR_end - NLR_start

    if length == 0:
        return []

    N = NLR[NLR_start]
    LNR_N_pos = LNR_quickpos[N]

    # LNR left interval = LNR_start, LNR_N_pos (might be length 0)
    # LNR right interval = LNR_N_pos+1, LNR_end (might be length 0)
    left_length = LNR_N_pos - LNR_start
    right_length = LNR_end - (LNR_N_pos+1)

    # NLR left interval = NLR_start+1, NLR_start+1+left_length
    # NLR right interval = NLR_start+1+left_length, NLR_end
    left_chunk  = get_LRN(NLR, NLR_start+1, NLR_start+1+left_length, LNR, LNR_start, LNR_N_pos, LNR_quickpos)
    n_chunk     = [N]
    right_chunk = get_LRN(NLR, NLR_start+1+left_length, NLR_end, LNR, LNR_N_pos+1, LNR_end, LNR_quickpos)

    return left_chunk + right_chunk + n_chunk
    

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(get_order([50, 30, 24, 5, 28, 45, 98, 52, 60]), [5, 28, 24, 45, 30, 60, 52, 98, 50])

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    nlr = [int(x) for x in sys.stdin.read().strip().split('\n')]
    lrn = [str(x) for x in get_order(nlr)]
    print("\n".join(lrn))

# Case-switch
if __name__ == '__main__':
    submit()