'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        outstring = ''
        number_string = len(strs)
        smallest_length = 1000
        for x in strs:
            if len(x)  < smallest_length:
                smallest_length = len(x)
        for i in range(smallest_length):
            flag = True
            first = strs[0][i]
            for j in range(1, len(strs)):
                if first != strs[j][i]:
                    flag = False
                    break
            if flag:
                outstring += first
            else:
                break
            
        
        return outstring
