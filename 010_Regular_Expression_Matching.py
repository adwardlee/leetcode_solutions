'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''Regular Expression Matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[[] for y in range(len(p)+1)] for x in range(len(s)+1)]
        dp[0][0] = 1
        index = 0
        for j in range(2,len(p)+1):
            if '*' == p[j - 1]:
                dp[index][j] = dp[index][j-2]
        
        while index < len(s):
            for j in range(len(p)):
                if dp[index][j] and (s[index] == p[j] or p[j] == '.'):
                    dp[index+1][j+1] = dp[index][j]

                if p[j] == '*' and j > 0 :
                    dp[index+1][j+1] = dp[index+1][j] or dp[index+1][j-1] or (dp[index][j] and (p[j-1] == s[index] or p[j-1] == '.')) or (dp[index][j + 1] and (s[index] == p[j - 1] or p[j-1] == '.'))
            
            index += 1
        return dp[len(s)][len(p)]
