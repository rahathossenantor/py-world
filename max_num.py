# finding the biggest number from a list
nums = [2, 8, 1, 45, 6, 4]
max_n = nums[0]
for num in nums:
    if num > max_n:
        max_n = num

print(max_n)
