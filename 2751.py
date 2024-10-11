# Implementation
def sorted_nums(nums):
    return sorted(nums)

# Testing
def test():
    print("WARNING: TEST MODE")

    assert sorted_nums([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    print("TEST DONE")

# Submit
def submit():
    import sys
    n = int(input())
    nums = [None] * n

    for i in range(n):
        nums[i] = int(sys.stdin.readline().strip())

    result = sorted_nums(nums)
    for x in result:
        print(x)

# Case-switch
if __name__ == '__main__':
    submit()