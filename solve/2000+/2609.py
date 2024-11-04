# Implementation
def gcd(a, b):
    if b > a:
        return gcd(b, a)
    
    assert a >= b
    
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

# Testing
assert gcd(24, 18) == 6
assert lcm(24, 18) == 72

assert gcd(12, 12) == 12
assert gcd(12, 11) == 1
assert gcd(12, 4) == 4
assert gcd(12, 1) == 1
assert gcd(12, 0) == 12

assert gcd(12, 12) == 12
assert gcd(11, 12) == 1
assert gcd(4, 12) == 4
assert gcd(1, 12) == 1
assert gcd(0, 12) == 12

# Input
a, b = list(map(int, input().split()))
print(gcd(a, b))
print(lcm(a, b))