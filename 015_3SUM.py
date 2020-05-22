'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums):
        outlist = []
        if len(nums) < 3:
            return []
        for idx, x in enumerate(nums):
            temp = self.twoSum(nums[idx + 1:], -x)
            if temp != []:
                for y in temp:
                    aa = y.copy()
                    aa.append(x)
                    temp1 = sorted(aa)
                    if temp1 not in outlist:
                            outlist.append(temp1)

        return outlist
             
    def twoSum(self, nums,target):
        output =[]
        for idx,x in enumerate(nums):
            if target - x in nums[idx+1:]:
                output.append([x, target - x])
        
        return output
