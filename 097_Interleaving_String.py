'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False
        dp = [[1 for i in range(l1+1)] for j in range(l2+1)]
        for i in range(1, l1+1):
            dp[0][i] = dp[0][i-1] and (s1[i-1] == s3[i-1])
        for i in range(1, l2+1):
            dp[i][0] = dp[i - 1][0] and (s2[i-1] == s3[i-1])
        for i in range(1, l2+1):
            for j in range(1, l1+1):
                dp[i][j] = (dp[i-1][j] and (s2[i-1] == s3[i + j - 1])) or (dp[i][j-1] and (s1[j-1] == s3[i + j - 1]))
            
        return dp[-1][-1]
