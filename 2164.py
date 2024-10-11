from collections import deque

# Implementation
def get_survived(n):
    queue = deque(range(1, n+1))

    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())

    return queue.popleft()

# Testing
def test():
    print("WARNING: TEST MODE")

    assert get_survived(6) == 4
    assert get_survived(4) == 4
    assert get_survived(2) == 2
    assert get_survived(1) == 1

    print("TEST DONE")

# Submit
def submit():
    n = int(input())
    print(get_survived(n))

# Case-switch
if __name__ == '__main__':
    submit()