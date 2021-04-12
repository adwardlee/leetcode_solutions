'''
Given a binary string s (a string consisting only of '0's and '1's), we can split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).

Return the number of ways s can be split such that the number of characters '1' is the same in s1, s2, and s3.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: s = "10101"
Output: 4
Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"
Example 2:

Input: s = "1001"
Output: 0
Example 3:

Input: s = "0000"
Output: 3
Explanation: There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"
Example 4:

Input: s = "100100010100110"
Output: 12
 

Constraints:

3 <= s.length <= 10^5
s[i] is '0' or '1'.
'''
class Solution:
    def numWays(self, s: str) -> int:
        length = len(s)
        one_count = 0
        split_range = {}
        for i in range(length):
            if s[i] == '1':
                one_count += 1
                
        if one_count % 3 != 0 or length < 3:
            return 0
        if one_count == 0:
            return (length - 2) * (length - 1) // 2 % (10 ** 9 + 7)
        
        for i in range(1, 3):
            split_range[i * one_count // 3] = i - 1
        one_count = 0
        split_index = [[] for i in range(2)]
        flag = False
        tmp_count = 0
        for i in range(length):
            if s[i] == '1':
                one_count += 1
                if flag == True:
                    split_index[tmp_count].append(i)
                    flag = False
            if s[i] == '1' and one_count in split_range:
                tmp_count = split_range[one_count]
                split_index[tmp_count].append(i)
                flag = True      
        
        
        output = (split_index[0][1] - split_index[0][0]) * (split_index[1][1] - split_index[1][0])
        
        return output % (10 ** 9 + 7)