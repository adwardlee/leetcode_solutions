'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

 

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return []

        word_dict = dict()
        out = []
        for x in words:
            if x not in word_dict:
                word_dict[x] = 1
            else:
                word_dict[x] += 1
        length = len(s)
        word_length = len(words[0])
        substring_length = len(words) * word_length
        
        for i in range(0, length - substring_length+1, 1):
            temp_dict = dict()
            for j in range(0,substring_length,word_length):
                x = s[i:i+substring_length][j:j+word_length]
                if x not in temp_dict:
                    temp_dict[x] = 1
                else:
                    temp_dict[x] += 1
            if temp_dict == word_dict:
                out.append(i)
        return out
