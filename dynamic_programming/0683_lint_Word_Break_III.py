'''
Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

Ignore case

Example
Example1

Input:
"CatMat"
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
Output: 3
Explanation:
we can form 3 sentences, as follows:
"CatMat" = "Cat" + "Mat"
"CatMat" = "Ca" + "tM" + "at"
"CatMat" = "C" + "at" + "Mat"
Example1

Input:
"a"
[]
Output: 
0
'''

class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
	O(n^2)
    """
    def wordBreak3(self, s, dict):
        # Write your code here
        s = s.lower()
        dicts = {}
        for x in dict:
            dicts[x.lower()] = 0
        self.dp = [0] * (len(s) + 1)
        self.dp[0] = 1
        for i in range(1, len(s) + 1):
            for j in range(i):
                if self.dp[j] and s[j:i] in dicts:
                    self.dp[i] += self.dp[j]
        return self.dp[-1]