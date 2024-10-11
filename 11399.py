# Implementation
''' write code here '''
def get_time(times):
    times = sorted(times)
    n, result = len(times), 0

    for i in range(n):
        result += times[i] * (n - i)

    return result

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    assert get_time([3, 1, 4, 3, 2]) == 32

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    _ = input()
    times = list(map(int, input().split()))

    print(get_time(times))

# Case-switch
if __name__ == '__main__':
    submit()