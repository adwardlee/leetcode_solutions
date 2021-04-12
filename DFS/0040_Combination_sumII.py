'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.output = []
        if sum(candidates) < target:
            return []
        self.candidates = sorted(candidates)
        self.length = len(candidates)
        count = 0
        tmp_sum = 0
        while count < self.length:
            if self.candidates[count] > target:
                break
            count += 1
        self.candidates = self.candidates[:count]
        self.length = count 
        self.backtracking([], 0, target)
        return self.output
        
    def backtracking(self, input_list, index, target):
        sums = sum(input_list)
        if sums == target:
            input_list = sorted(input_list)
            if input_list not in self.output:
                self.output.append(input_list)
            else:
                return
        elif sums > target:
            return
        for x in range(index, self.length):
            self.backtracking(input_list + [self.candidates[x]], x + 1, target)
            
        return