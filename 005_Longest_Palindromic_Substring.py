'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

class Solution:
    def substring(self, i, index, s):
        while i >=1 and index < len(s) - 1:
            if s[i - 1] == s[index + 1]:
                i -= 1
                index += 1
            else:
                break
            
        return i, index+1
        
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        max_len = 0
        final_start = len(s)
        final_end = 0
        for i in range(len(s) - 1):
            index = i
            while index < len(s) - 1 and s[index + 1] == s[i]:
                index += 1
            start, end = self.substring(i,index,s)
            if end - start > final_end - final_start:
                final_end = end
                final_start = start
                
        return s[final_start:final_end]
    
