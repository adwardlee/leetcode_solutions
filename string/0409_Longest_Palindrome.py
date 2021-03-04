class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashdict = dict()
        for x in s:
            if x not in hashdict:
                hashdict[x] = 1
            else:
                hashdict[x] += 1
        longest = 0
        odd_flag = 0
        for key, value in hashdict.items():
            if value % 2 == 0:
                longest += value
            elif odd_flag == 0:
                longest += value
                odd_flag = 1
            else:
                longest += value - 1
        return longest
'''
hashtable to record frequency of alphabets
even to increase the longest length
'''

'''
Time: O(n)
Space: O(n)
'''
