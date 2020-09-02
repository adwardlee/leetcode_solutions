'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s = len(s)
        len_t = len(t)
        if len_s < len(t) or len(t) == 0:
            return ''
        left = 0
        right = 0
        min_len = [len_s + 1,[-1,-1]]
        one_dict = {}
        for x in t:
            if x not in one_dict:
                one_dict[x] = 1
            else:
                one_dict[x] += 1
        tmp = one_dict
        while right < len(s):
            if s[right] in tmp:
                tmp[s[right]] -= 1
            if self.allTrue(tmp):
                while left <= right:
                    if s[left] in tmp:
                        tmp[s[left]] += 1
                    
                    if not self.allTrue(tmp):
                        if right - left + 1 < min_len[0]:
                            min_len[0] = right - left + 1
                            min_len[1] = [left, right]
                        left += 1
                        break
                    left += 1
                    
            right += 1
        if min_len[0] <= len_s:
            return s[min_len[1][0]:min_len[1][1] + 1]
        else:
            return ''
            
    def allTrue(self, one_dict):
        x = True
        for key in one_dict:
            if one_dict[key] > 0:
                x = False
        return x
