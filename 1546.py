# Implementation
def new_average(L):
    return (sum(L) / len(L)) * (100 / max(L))

# Testing
assert 74.9 <= new_average([40, 80, 60]) <= 75.1

# Input
n = int(input())
L = list(map(int, input().split()))
assert len(L) == n
print(new_average(L))