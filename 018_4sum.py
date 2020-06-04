'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution:
    def __init__(self):
        self.final_out = []
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        idx = 0
        while idx < len(nums) -3:
            if idx > 0 and nums[idx] == nums[idx - 1]:
                idx += 1
                continue
            x = nums[idx]
            target1 = target - x
            temp = [x]
            self.Sums(nums[idx+1:], target1,2, temp)
            idx += 1
           
        return self.final_out
    
    def Sums(self, num_array, target, numbers, halfset):
        if len(num_array) == 0:
            return 
        temp = []
        temp.extend(halfset)
        if numbers == 0:
            if target in num_array:
                temp.append(target)
                self.final_out.append(temp)
            return 
        idx = 0
        while idx < len(num_array) - numbers:
            if idx > 0 and num_array[idx] == num_array[idx - 1]:
                idx += 1
                continue
            x = num_array[idx]
            target1 = target -x
            
            temp.append(x)
            self.Sums(num_array[idx+1:], target1, numbers - 1, temp)
            temp.pop()
            idx += 1
        return
            
        
        
