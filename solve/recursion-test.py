import sys, cProfile
sys.setrecursionlimit(100000)

def recursion(n):
    if n == 0:
        return 0
    return n + recursion(n-1)

def loop(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

print(recursion(90000))
# print(loop(90000))

# cProfile.run('recursion(90000)')
# cProfile.run('loop(90000)')