'''
uppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        elif len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right + 1) // 2
            if nums[mid] == target:
                return True
            if left == right:
                break
            if nums[left] == nums[mid]:
                while left < right and nums[left] == nums[mid]:
                    left += 1
            else:

                if nums[mid] >= nums[left]:
                    if target >= nums[left] and target <= nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if target >= nums[mid] and target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False
        
