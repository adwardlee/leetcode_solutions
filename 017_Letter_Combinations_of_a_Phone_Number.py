'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution:
    def __init__(self):
        self.output = []
        self.dicts = {'2': 'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv','9':'wxyz'}
    def letterCombinations(self, digits: str) -> List[str]:
        x = ''
        self.backtrack(digits, x)
        return self.output
        
    def backtrack(self, digits, one):
        if digits == '':
            if one == '':
                return
            else:
                self.output.append(one)
            return 
            
        if digits[0] in self.dicts:
            for x in self.dicts[digits[0]]:
                self.backtrack(digits[1:], one + x)
