'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_ind = 0
        max_num = [0, 0]
        steps = 0
        while cur_ind < len(nums) - 1:
            for idx, i in enumerate(range(1, nums[cur_ind] + 1)):
                if cur_ind + i >= len(nums) - 1:
                    return steps + 1
                if nums[cur_ind + i] + cur_ind + i > max_num[1]:
                    max_num = [cur_ind + i, nums[cur_ind + i] + cur_ind + i]
            steps += 1
            cur_ind = max_num[0]
            max_num = [0, 0]
        return steps
        
