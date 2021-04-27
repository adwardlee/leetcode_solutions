'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109
 

Follow up: Could you implement the O(n) solution?
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        self.dict = {}
        for x in nums:
            self.dict[x] = [x - 1, x + 1]
        visited_dict = {}
        longest_list = []
        max_len = 1
        for key in self.dict.keys():
            if key not in visited_dict:
                visited_dict[key] = 0
                longest_list.append(key)
                self.recursive([key], longest_list,visited_dict)

                if len(longest_list) > max_len:
                    max_len = len(longest_list)
            longest_list = []
        return max_len

    def recursive(self, key, longest_list, visited_dict):
        while key != []:
            tmp = []
            for one in key:
                for otherkey in self.dict[one]:
                    if otherkey in self.dict and otherkey not in visited_dict:
                        tmp.append(otherkey)
                        longest_list.append(otherkey)
                        visited_dict[otherkey] = 0
            key = tmp
        return