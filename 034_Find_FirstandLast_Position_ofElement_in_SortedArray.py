'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        output = []
        while left <= right:
            if nums[left] == target and target == nums[right]:
                return [left, right]
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1  
            elif nums[mid] < target:
                left = mid + 1
            else:
                right_temp = (right + mid) // 2

                while nums[right_temp] == nums[mid]:
                    if right_temp < right:
                        right_temp = (right + right_temp) // 2 + 1
                    else:
                        right_temp += 1
                        break
                right = right_temp - 1
                
                left_temp = (left + mid) // 2
                while nums[left_temp] == nums[mid]:
                    if left_temp > left:
                        left_temp = (left + left_temp) // 2
                    else:
                        left_temp -= 1
                        break
                left = left_temp + 1
                
        return [-1,-1]
