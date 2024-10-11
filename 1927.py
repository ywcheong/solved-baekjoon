# Header
''' import header here '''
import heapq

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
def step(heap, task):
    output = None

    if task == 0:
        if len(heap) > 0:
            output = heapq.heappop(heap)
        else:
            output = 0
    else:
        heapq.heappush(heap, task)

    return heap, output

def simulate(tasks):
    heap, result = [], []

    for task in tasks:
        heap, output = step(heap, task)
        if output is not None:
            result.append(output)

    return result

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    tasks = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]
    equal(simulate(tasks), [0, 1, 2, 12345678, 0])

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    T = int(input())
    tasks = [None] * T
    for i in range(T):
        tasks[i] = int(input())
    print("\n".join(map(str, simulate(tasks))))

# Case-switch
if __name__ == '__main__':
    submit()