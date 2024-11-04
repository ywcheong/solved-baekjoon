# Implementation
def simulate_step(this: set, task: str):
    output = None
    params = task.split()

    if params[0] == 'add':
        x = int(params[1])
        this = this | {x}
    elif params[0] == 'remove':
        x = int(params[1])
        this = this - {x}
    elif params[0] == 'check':
        x = int(params[1])
        output = 1 if x in this else 0
    elif params[0] == 'toggle':
        x = int(params[1])
        if x in this:
            this = this - {x}
        else:
            this = this | {x}
    elif params[0] == 'all':
        this = set(range(1, 21))
    elif params[0] == 'empty':
        this = set()
    else:
        raise Exception(task)

    return this, output

# Testing
def test():
    print("WARNING: TEST MODE")

    test_tasks_1 = ['add 1', 'add 2', 'check 1', 'check 2', 'check 3', 'remove 2', 'check 1', 'check 2', 'toggle 3', 'check 1', 'check 2', 'check 3', 'check 4', 'all', 'check 10', 'check 20', 'toggle 10', 'remove 20', 'check 10', 'check 20', 'empty', 'check 1', 'toggle 1', 'check 1', 'toggle 1', 'check 1']
    test_result_1 = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0]

    assert simulate(test_tasks_1) == test_result_1

    print("TEST DONE")

# Submit
def submit():
    import sys

    n = int(input())
    this = set()

    for _ in range(n):
        task = sys.stdin.readline().strip()
        this, output = simulate_step(this, task)
        if output is not None:
            print(output)

# Case-switch
if __name__ == '__main__':
    submit()