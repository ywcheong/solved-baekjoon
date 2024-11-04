# Implementation
def is_vps(text):
    depth = 0
    for s in text:
        if s == '(':
            depth += 1
        elif s == ')':
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

# Testing
def test():
    print("WARNING: TEST MODE")

    # Case 1
    assert is_vps('(())())') == False
    assert is_vps('(((()())()') == False
    assert is_vps('(()())((()))') == True
    assert is_vps('((()()(()))(((())))()') == False
    assert is_vps('()()()()(()()())()') == True
    assert is_vps('(()((())()(') == False

    # Case 2
    assert is_vps('((') == False
    assert is_vps('))') == False
    assert is_vps('())(()') == False

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    n = int(input())

    for _ in range(n):
        print("YES" if is_vps(input()) else "NO")

# Case-switch
if __name__ == '__main__':
    submit()