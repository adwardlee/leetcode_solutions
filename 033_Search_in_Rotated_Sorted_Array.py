'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution:
    def search(self, nums, target: int) -> int:
        self.nums = nums
        length = len(nums)
        if length == 0:
            return -1
        left = 0
        right = length - 1
        mid = (left + right) // 2
        return max(self.quicksort(left, mid, target), self.quicksort(mid + 1, right, target))

    def quicksort(self, left, right, target):
        if left > right:
            return -1
        if left == right:
            if self.nums[left] == target:
                return left
            else:
                return -1
        mid = (left + right) // 2
        if self.nums[mid] == target:
            return mid
        if self.nums[left] < self.nums[right]:
            if self.nums[left] <= target and target <= self.nums[right]:
                return max(self.quicksort(left, mid, target), self.quicksort(mid + 1, right, target))
            else:
                return -1
        else:
            if self.nums[left] > target and self.nums[right] < target:
                return -1
            else:
                return max(self.quicksort(left, mid, target), self.quicksort(mid + 1, right, target))
