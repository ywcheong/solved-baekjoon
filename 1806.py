n, s = map(int, input().split())
nums = list(map(int, input().split()))
assert len(nums) == n

# [start, end)의 반열린 구간에 대한 합 산출
start, end = 0, 0
sum = 0

# 최소 길이 저장
shortest = 987654321

while end <= n:
    if sum >= s:
        shortest = min(shortest, end - start)
        sum -= nums[start]
        start += 1
    elif end < n:
        sum += nums[end]
        end += 1
    else:
        break

if shortest == 987654321:
    shortest = 0

print(shortest)