class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        duration = len(needle)
        if duration == 0:
            return 0
        if len(haystack) < duration:
            return -1
        target = 0
        tmp_target = 0
        for i in range(duration):
            target = target * 29 + (ord(needle[i]) - ord('a') )
            tmp_target = tmp_target * 29 + ord(haystack[i]) - ord('a')
        if target == tmp_target:
            return 0
        start = 0
        for i in range(duration, len(haystack)):
            tmp_target = (tmp_target - (ord(haystack[start]) - ord('a')) * 29 ** (duration - 1))* 29 + ord(haystack[i]) - ord('a')
            start += 1
            if tmp_target == target:
                return start
        return -1
        '''
        if needle == '':
            return 0
        start = 0
        duration = len(needle)
        for i in range(len(haystack) - duration+1):
            if haystack[i:i+duration] == needle:
                return i
        
        return -1
        '''
'''
first rabin-karp algo: time O(n + m), space O(1)
second direct string comparison: time O(n * m), space O(m)
'''
