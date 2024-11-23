# My Solution : https://github.com/ywcheong/solved-baekjoon

# Header
''' import header here '''
from collections import Counter

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
def get_sequence(L, pick_amount):
    L = sorted(L)
    is_picked = [False] * len(L)

    # Backtrack cursor
    current_sequence = [None] * pick_amount

    # Apply Backtrack algorithm
    def backtrack(sequence_index):
        # Good End: Completed
        if sequence_index == pick_amount:
            result.append(tuple(current_sequence))
            return

        # Searching
        
        # There are duplicates in L, so prevent duplicates
        last_picked_element = None

        for picked_index, picked_element in enumerate(L):
            # Skip if already used to forwardtracking
            if picked_element == last_picked_element:
                continue
            
            # Cannot use already-used value
            if is_picked[picked_index]:
                continue

            # Now go for it
            last_picked_element = picked_element
            
            # Forward-search-back
            is_picked[picked_index] = True
            current_sequence[sequence_index] = picked_element
            backtrack(sequence_index + 1)
            is_picked[picked_index] = False

    result = []
    backtrack(0)

    return result

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> 
    equal(get_sequence([4, 4, 2], 1), [
        (2,),
        (4,)
    ])

    equal(get_sequence([9, 7, 9, 1], 2), [
        (1, 7),
        (1, 9),
        (7, 1), 
        (7, 9),
        (9, 1),
        (9, 7),
        (9, 9),
    ])

    equal(get_sequence([1, 1, 1, 1], 4), [
        (1, 1, 1, 1,),
    ])

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    N, pick_amount = input_list(int)
    L = input_list(int)

    assert len(L) == N
    sequences = get_sequence(L, pick_amount)
    str_sequences = [" ".join(map(str, seq)) for seq in sequences]
    print("\n".join(str_sequences))

# Case-switch
if __name__ == '__main__':
    submit()