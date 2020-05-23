'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        closest = 10**10
        output = 0
        for idx, x in enumerate(nums):
            if idx > 0 and nums[idx - 1] == nums[idx]:
                continue
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                sums = x + nums[l] + nums[r]
                subtraction = abs(sums - target)
                if sums < target:
                    if subtraction < abs(closest):
                        closest = subtraction
                        output = sums
                    l += 1
                elif sums > target:
                    if subtraction < abs(closest):
                        closest = subtraction
                        output = sums
                    r -= 1
                else:
                    return target
        return output
