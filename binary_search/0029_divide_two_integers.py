'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
'''

#### 1 ####
import math
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        flag = 1
        if dividend * divisor < 0:
            flag = -1
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor
        if dividend == 0:
            return 0
        return flag * int(math.exp(math.log(dividend) - math.log(divisor))+ 1e-13)
		
#### 2 ####
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = 1
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        if dividend * divisor < 0:
            flag = -1
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor
        return flag * self.numberDivid(dividend, divisor)

    def numberDivid(self, dividend, divisor):
        count = 0
        sum_count = divisor
        remain = dividend - sum_count
        if remain >= 0:
            count = 1
        while dividend - sum_count >= sum_count:
            sum_count += sum_count
            count += count
            remain = dividend - sum_count
        if remain > 0:
            return count + self.numberDivid(remain, divisor)
        else:
            return count