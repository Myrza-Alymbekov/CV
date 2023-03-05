nums = [1, 2, 3, 6, 7]

for i in nums:
    nums[nums.index(i)] = str(i)

print(nums)

for i in nums:
    nums[nums.index(i)] = int(i)
    
print(nums)