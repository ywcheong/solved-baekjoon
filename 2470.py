def score(nums, a, b):
    return abs(nums[a] + nums[b])

n = int(input())
nums = list(map(int, input().split()))
assert len(nums) == n

nums.sort()

result = (0, n-1)
left, right = 0, n-1
while left < right:
    # print(f"nums[{left}] = {nums[left]}, nums[{right}] = {nums[right]}")
    # 판정 단계
    if score(nums, left, right) < score(nums, *result):
        result = (left, right)

    # 이동 단계
    sum = nums[left] + nums[right]
    if sum > 0:
        right -= 1
    elif sum < 0:
        left += 1
    else:
        break

print(nums[result[0]], nums[result[1]])