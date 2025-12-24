from collections import deque


# Implementation
def simulate_step(stack: deque, task: str):
    output = None

    if task.startswith("push"):
        _, param_str = task.split()
        param_int = int(param_str)
        stack.append(param_int)
    elif task == "pop":
        if len(stack) > 0:
            output = stack[-1]
            stack.pop()
        else:
            output = -1
    elif task == "size":
        output = len(stack)
    elif task == "empty":
        output = 1 if len(stack) == 0 else 0
    elif task == "top":
        if len(stack) > 0:
            output = stack[-1]
        else:
            output = -1
    else:
        raise Exception(task)

    return stack, output


def simulate(tasks):
    stack = deque()
    result = []

    for task in tasks:
        stack, output = simulate_step(stack, task)
        if output is not None:
            result.append(str(output))

    return result

# Testing
def test():
    print("WARNING: TEST MODE")

    test_tasks_1 = ['push 1', 'push 2', 'top', 'size', 'empty', 'pop', 'pop', 'pop', 'size', 'empty', 'pop', 'push 3', 'empty', 'top']
    test_result_1 = [2, 2, 0, 2, 1, -1, 0, 1, -1, 0, 3]

    test_tasks_2 = ['pop', 'top', 'push 123', 'top', 'pop', 'top', 'pop']
    test_result_2 = [-1, -1, 123, 123, -1, -1]

    assert simulate(test_tasks_1) == test_result_1
    assert simulate(test_tasks_2) == test_result_2

    print("TEST DONE")

# Submit
def submit():
    import sys

    n = int(input())
    tasks = [None] * n

    for i in range(n):
        tasks[i] = sys.stdin.readline().strip()

    print("\n".join(simulate(tasks)))

# Case-switch
if __name__ == '__main__':
    submit()