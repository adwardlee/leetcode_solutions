'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.length = len(nums)
        if self.length == 0:
            return []
        self.dfs(nums,[])
        return self.output
    
    def dfs(self, nums, cur):
        if len(cur) == self.length:
            if cur not in self.output:
                self.output.append(cur)
            return 
        for i, x in enumerate(nums):
            self.dfs(nums[:i] + nums[i+1:], cur + [x])
        return
