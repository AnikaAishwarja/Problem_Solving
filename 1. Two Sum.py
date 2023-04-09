nums = [1,2,3,4]
target = int(input())

for i in range(len(nums)):
  for j in range(i+1,len(nums)):
    if (nums[i]!=nums[j]) and (nums[i] + nums[j] == target):
      print(nums[i],nums[j])