from collections import deque


# Implementation
def simulate_step(queue: deque, task: str):
    output = None

    if task.startswith("push"):
        _, param_str = task.split()
        param_int = int(param_str)
        queue.append(param_int)
    elif task == "pop":
        if len(queue) > 0:
            output = queue[0]
            queue.popleft()
        else:
            output = -1
    elif task == "size":
        output = len(queue)
    elif task == "empty":
        output = 1 if len(queue) == 0 else 0
    elif task == "front":
        if len(queue) > 0:
            output = queue[0]
        else:
            output = -1
    elif task == "back":
        if len(queue) > 0:
            output = queue[len(queue) - 1]
        else:
            output = -1
    else:
        raise Exception(task)

    return queue, output


def simulate(tasks):
    queue = deque()
    result = []

    for task in tasks:
        queue, output = simulate_step(queue, task)
        if output is not None:
            result.append(str(output))

    return result


# Testing
def test():
    print("WARNING: TEST MODE")

    test_tasks = [
        "push 1",
        "push 2",
        "front",
        "back",
        "size",
        "empty",
        "pop",
        "pop",
        "pop",
        "size",
        "empty",
        "pop",
        "push 3",
        "empty",
        "front",
    ]

    test_result = [1, 2, 2, 0, 1, 2, -1, 0, 1, -1, 0, 3]

    assert simulate(test_tasks) == test_result

    print("TEST DONE")


# Submit
def submit():
    """get input here"""
    import sys

    n = int(input())
    tasks = [None] * n

    for i in range(n):
        tasks[i] = sys.stdin.readline().strip()

    print("\n".join(simulate(tasks)))


# Case-switch
if __name__ == "__main__":
    submit()
