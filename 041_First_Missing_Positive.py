'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
'''

class Solution:
    def firstMissingPositive(self, nums):
        length = len(nums)
        for i in range(length):
            if nums[i] <= length and nums[i] > 0:
                temp = nums[nums[i] - 1]
                if temp == nums[i]:
                    continue
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
                while nums[i] < i + 1 and nums[i] <= length and nums[i] > 0:
                    temp1 = nums[nums[i] - 1]
                    if temp1 == temp:
                        break
                    nums[nums[i] - 1] = temp
                    nums[i] = temp1
                    temp = nums[i]
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1
