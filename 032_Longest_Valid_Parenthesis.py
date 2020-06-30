'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length = len(s)
        if length == 0 or length == 1:
            return 0
        index = 0
        stack = [[-1, -1]]
        max_length = 0
        while index < length:
            if len(stack) == 0:
                stack.append([s[index],index])
                index += 1
                continue
            
            if stack[-1][0] == '(' and s[index] == ')':
                stack.pop()
                max_length = max(max_length, index - stack[-1][1])
            else:
                stack.append([s[index],index])
            index += 1
        
        
        
        return max_length
