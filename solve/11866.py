# Implementation
from collections import deque

def get_josephus(N, K):
    queue = deque(range(1, N+1))
    result = []
    while len(queue) > 1:
        for turn in range(K):
            if turn != K-1:
                queue.append(queue.popleft())
            else:
                result.append(queue.popleft())
    return result + [queue[0]]

# Testing
def test():
    print("WARNING: TEST MODE")

    assert get_josephus(7, 3) == [3, 6, 2, 7, 5, 1, 4]

    print("TEST DONE")

# Submit
def submit():
    N, K = list(map(int, input().split()))
    print(f'<{", ".join(list(map(str, get_josephus(N, K))))}>')

# Case-switch
if __name__ == '__main__':
    submit()