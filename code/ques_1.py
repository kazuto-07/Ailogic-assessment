def search(nums,target):
    if target not in nums:
      return -1
    else:
      for i in nums: 
         if i == target:
            return nums.index(i)