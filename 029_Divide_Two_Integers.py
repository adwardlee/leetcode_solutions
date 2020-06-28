'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1]. For the purpose of this problem, assume that your function returns 2**31 − 1 when the division result overflows.
'''
import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == 0:
            return 0
        if (dividend > 0 and divisor >0) or (dividend <0 and divisor <0):
            flag = 1
        else:
            flag = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        temp = divisor
        quotient = 0
        count = 1
        while dividend >= divisor:
            temp = temp << 1
            count = count << 1
            if temp > dividend:
                dividend -= temp >> 1
                count = count >> 1
                quotient += count
                count = 1
                temp = divisor

        if flag:
            return quotient
        else:
            return -quotient
