'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == ' ' or len(s) == 0:
            return 0
        if s[-1] != ' ':
            return len(s.split(' ')[-1])
        else:
            tmp = s.split(' ')
            index = len(tmp) - 1
            while tmp[index] == '':
                index -= 1
                if index == -1:
                    return 0
            return len(tmp[index])
