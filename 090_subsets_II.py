'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = nums[::-1]
        final_list = [[]]
        while len(nums) > 0:
            one = nums.pop()
            for x in final_list.copy():
                tmp = sorted(x + [one])
                if tmp not in final_list:
                    final_list.append(tmp)
        return final_list
