'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
'''
import numpy as np
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length == 1:
            return s
        elif length == 2:
            return s[0] if s[0] != s[1] else s
        max_value = 0
        max_pos = 0
        max_substring = s[0]
        for i in range(1, length - 1):
            value, substring = max(self.expand_palindrome(i, i+1, s, length), self.expand_palindrome(i - 1, i + 1, s, length),  self.expand_palindrome(i - 1, i, s, length)) 
            if value > max_value:
                max_value = value
                max_substring = substring
        return max_substring

    
    def expand_palindrome(self, left, right, s, length):
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1, s[left + 1:right]
'''
from center to two end
Time: O(n^2)
Space: O(n)
'''
