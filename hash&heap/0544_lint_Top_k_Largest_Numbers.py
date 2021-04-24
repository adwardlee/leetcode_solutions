'''
Description
Given an integer array, find the top k largest numbers in it.

Example
Example1

Input: [3, 10, 1000, -99, 4, 100] and k = 3
Output: [1000, 100, 10]
Example2

Input: [8, 7, 6, 5, 4, 3, 2, 1] and k = 5
Output: [8, 7, 6, 5, 4]
'''

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def partition(self, nums, left, right):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i


    def quickSelect(self, nums, left, right, k):
        if left <= right:
            mid = self.partition(nums, left, right)
            if mid - left == k:
                return nums[mid:]
            elif mid - left > k:
                return self.quickSelect(nums, left , mid - 1, k)
            return self.quickSelect(nums, mid + 1, right, k - 1 - (mid - left))

        return

    def topk(self, nums, k):
        # write your code here
        if k == 0 or len(nums) == 0 or len(nums) < k:
            return [-1]
        left = 0
        right = len(nums) - 1
        k = right + 1 - k
        return sorted(self.quickSelect(nums, left, right, k))[::-1]