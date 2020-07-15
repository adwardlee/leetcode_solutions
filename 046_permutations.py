'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.length = len(nums)
        self.dfs(nums, [])
        return self.output
    
    def dfs(self, nums, output):
        if len(output) == self.length:
            self.output.append(output[:])
            return
        for idx, i in enumerate(nums):
            self.dfs(nums[:idx] + nums[idx+1:], output + [i])
        return 
