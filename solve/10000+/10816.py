# Implementation
def get_count(deck, target):
    count = dict()
    for num in deck:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    result = [0] * len(target)
    for i in range(len(target)):
        if target[i] in count:
            result[i] = count[target[i]]
    
    return result


# Testing
def test():
    print("WARNING: TEST MODE")

    assert get_count([6, 3, 2, 10, 10, 10, -10, -10, 7, 3], [10, 9, -5, 2, 3, 4, 5, -10]) == [3, 0, 0, 1, 2, 0, 0, 2]

    print("TEST DONE")

# Submit
def submit():
    _ = input()
    deck = list(map(int, input().split()))
    _ = input()
    target = list(map(int, input().split()))

    print(" ".join(map(str, get_count(deck, target))))

# Case-switch
if __name__ == '__main__':
    submit()