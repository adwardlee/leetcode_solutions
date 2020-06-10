'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.output = []
        self.n = n
        self.backtrack('',0,0)
        return self.output
        
        
    def backtrack(self, cur_str, left, right):
        if right > left:
            return 
        elif left - right > self.n * 2 - len(cur_str):
            return
        if left ==self.n and right == self.n:
            self.output.append(cur_str)
            return

        self.backtrack(cur_str + '(', left +1 , right)
        self.backtrack(cur_str + ')', left, right+1)
