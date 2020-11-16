'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.
Example 4:

Input: s = "1"
Output: 1
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        if int(s[0]) == 0:
            return 0
        elif len(s) < 2:
            return 1
        if int(s[1]) == 0:
            if int(s[0]) < 3:
                dp[0] = 1
                dp[1] = 1
            else:
                return 0
        elif int(s[:2]) > 10 and int(s[:2]) < 27:
                dp[0] = 1
                dp[1] = 2
        elif int(s[:2]) < 10 and int(s[:2]) > 0:
                dp[0] = 0
                dp[1] = 1
        else:
                dp[0] = 1
                dp[1] = 1
        
        for i in range(2, len(s)):
            if int(s[i]) > 0 and int(s[i]) < 10:
                dp[i] += dp[i - 1]
            if int(s[i - 1]) == 1 or (int(s[i - 1]) == 2 and int(s[i]) < 7):
                dp[i] += dp[i - 2]
            
        return dp[len(s) - 1]
