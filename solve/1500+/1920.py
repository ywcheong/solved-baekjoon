# Implementation
def is_exist(source, target):
    source = set(source)
    return [(1 if x in source else 0) for x in target]

# Testing
def test():
    print("WARNING: TEST MODE")

    assert is_exist([4, 1, 5, 2, 3], [1, 3, 7, 9, 5]) == [1, 1, 0, 0, 1]

    print("TEST DONE")

# Submit
def submit():
    _ = input()
    source = list(map(int, input().split()))
    _ = input()
    target = list(map(int, input().split()))

    result = is_exist(source, target)
    print("\n".join(list(map(str, result))))

# Case-switch
if __name__ == '__main__':
    submit()