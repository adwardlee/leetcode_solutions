'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s)
        len_p = len(p)
        dp = [[0] * (len_s + 1) for i in range(len_p + 1 )]
        dp[0][0] = 1
        index = 0
        for j in range(len_p):
            if p[j] == '*':
                dp[j + 1][0] = dp[j][0]
                dp[j + 1][index] = dp[j][index]

            for i in range(index, len_s):
                if s[i] == p[j] or p[j] == '?':
                    dp[j + 1][i + 1] = dp[j][i]
                elif p[j] == '*':
                    dp[j + 1][i + 1] = dp[j][i + 1] or dp[j + 1][i]

        return dp[len_p][len_s]
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s)
        len_p = len(p)
        dp = [[0] * (len_s + 1) for i in range(len_p + 1 )]
        dp[0][0] = 1
        index = 0
        for j in range(len_p):
            if p[j] == '*':
                dp[j + 1][0] = dp[j][0]
                dp[j + 1][index] = dp[j][index]

            for i in range(index, len_s):
                if s[i] == p[j] or p[j] == '?':
                    dp[j + 1][i + 1] = dp[j][i]
                elif p[j] == '*':
                    dp[j + 1][i + 1] = dp[j][i + 1] or dp[j + 1][i]

        return dp[len_p][len_s]
