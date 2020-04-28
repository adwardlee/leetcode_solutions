'''Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        positive = 1
        if x < 0:
            positive = 0
        temp = str(x)
        while temp[-1] == '0':
            temp = temp[:-1]
        if positive:
            out  = int(temp[::-1])
            if out > (2 ** 31 -1):
                return 0
            else:
                return out
        else:
            out = int('-' + temp[1:][::-1])
            if out < -2**31:
                return 0
            else:
                return out
