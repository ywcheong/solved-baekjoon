def isPrime(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    for x in range(2, n):
        if n % x == 0:
            return 0
        
    return 1

_ = input()
nums = map(isPrime, map(int, input().split()))
print(sum(nums))