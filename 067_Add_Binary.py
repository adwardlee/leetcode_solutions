'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            return self.addBinary(b, a)
        max_len = len(a)
        result = ''
        rest = 0
        a = a[::-1]
        b = b[::-1]
        for idx in range(max_len):
            if idx >= len(b):
                tmp = int(a[idx]) + rest
                if tmp >= 2:
                    rest = 1
                    result = '0' + result
                else:
                    rest = 0
                    result = str(tmp) + result
            else:
                tmp = int(a[idx]) + int(b[idx]) + rest
                if tmp == 3:
                    rest = 1
                    result = '1' + result
                elif tmp == 2:
                    rest = 1
                    result = '0' + result
                else:
                    rest = 0
                    result = str(tmp) + result
        if rest == 1:
            result = '1' + result
        if result[0] == '0' and len(result) > 1:
            result = result[1:]
        return result
                
                
