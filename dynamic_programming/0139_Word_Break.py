'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
	    '''
		O(n^2)
		'''
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            temp = False
            for j in range(0, i):
                temp  = temp or (dp[j] and s[j:i] in wordDict)
            dp[i] = temp
        return dp[len(s)]
		
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
	    '''
		O(n^3)
		'''
        self.dict = {}
        self.memo = [[False] * len(s) for i in range(len(s))]
        for x in wordDict:
            self.dict[x] = 0
        for i in range(len(s) -1, -1, -1):
            for j in range(i, len(s)):
                tmp = s[i:j + 1] in self.dict
                if tmp == True:
                    self.memo[i][j] = True
                    continue
                for k in range(i, j):
                     self.memo[i][j] = self.memo[i][j] or ((s[i:k+1] in self.dict) and self.memo[k+1][j])

        return self.memo[0][len(s) - 1]