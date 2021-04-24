'''
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
 

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
'''

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.output = set()
        self.length = 0
        flag, left, right = self.isValid(s)
        if flag:
            return [s]
        self.dfs(left, right, 0, s)
        return list(self.output)
        
    def dfs(self, leftcount, rightcount, start, string):
        if leftcount == 0 and rightcount == 0 and self.isValid(string)[0]:
            if len(string) > self.length:
                self.output = set([string])
                self.length = len(string)
            elif len(string) == self.length:
                self.output.add(string)
            return
        if leftcount > len(string) or rightcount > len(string) or len(string) < self.length:
            return
        for i in range(start, len(string)):
            if i > 0 and string[i] == string[i - 1]:
                continue
            if string[i] == '(' and leftcount > 0:
                self.dfs(leftcount - 1, rightcount, i, string[:i] + string[i+1:])
            elif string[i] == ')' and rightcount > 0:
                self.dfs(leftcount, rightcount - 1, i, string[:i] + string[i+1:])
            
        return
        
    def isValid(self, string):
        left_count = 0
        right_count = 0
        for x in string:
            if x == '(':
                left_count += 1
            elif x == ')':
                if left_count > 0:
                    left_count -= 1
                else:
                    right_count += 1
        if left_count == 0 and right_count == 0:
            return True, left_count, right_count
        return False, left_count, right_count