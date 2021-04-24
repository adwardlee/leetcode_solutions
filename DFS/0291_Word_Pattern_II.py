'''
Description
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to s, then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)

You may assume both pattern and str contains only lowercase letters.

Example
Example 1

Input:
pattern = "abab"
str = "redblueredblue"
Output: true
Explanation: "a"->"red","b"->"blue"
Example 2

Input:
pattern = "aaaa"
str = "asdasdasdasd"
Output: true
Explanation: "a"->"asd"
Example 3

Input:
pattern = "aabb"
str = "xyzabcxzyabc"
Output: false

'''

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, string):
        # write your code here
        p2w = {}
        w2p = {}
        out = self.backtracking(pattern, string, 0, 0, p2w, w2p)
        return out 

    def backtracking(self, pattern, string, pindex, windex, p2w, w2p):
        isMatch = False
        if len(pattern) == pindex and len(string) == windex:
            return True
        elif len(pattern) == pindex or len(string) == windex:
            return False
        if pattern[pindex] in p2w:
            word = string[windex: windex + len(p2w[pattern[pindex]])]
            if word == p2w[pattern[pindex]]:
                isMatch = self.backtracking(pattern, string, pindex + 1, windex + len(p2w[pattern[pindex]]), p2w, w2p)

        else:
            for i in range(windex, len(string)):
                word = string[windex: i+1]
                if word in w2p:
                    continue
                p2w[pattern[pindex]] = word
                w2p[word] = pattern[pindex]
                isMatch = self.backtracking(pattern, string, pindex + 1, i+1, p2w, w2p)
                if isMatch == True:
                    break
                p2w.pop(pattern[pindex])
                w2p.pop(word)


        return isMatch