'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.output = []
        self.dict = {}
        for x in wordDict:
            self.dict[x] = 0
        self.dfs(s, 0, [])
        return self.output

    def dfs(self, word, index, exist_list):
        if index == len(word):
            self.output.append(' '.join(exist_list))
            return
        for i in range(index + 1, len(word)+1):
            if word[index:i] in self.dict:
                exist_list.append(word[index:i])
                self.dfs(word, i, exist_list)
                exist_list.pop()
        return