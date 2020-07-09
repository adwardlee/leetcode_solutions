'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        self.candidates = sorted(candidates)
        self.length = len(candidates)
        self.dfs(0, [], target, 0)
        return self.output
        
    def dfs(self, sums, nums, target, index):
        if sums == target:
            if nums not in self.output:
                self.output.append(nums.copy())
            return True
        if sums > target:
            return False
        if index >= self.length:
            return False
        for idx, x in enumerate(self.candidates[index:]):
            sums += x
            nums.append(x)
            if self.dfs(sums, nums, target, index + 1 + idx):
                sums -= x
                nums.pop()
                break
            else:
                sums -= x
                nums.pop()
        return False
