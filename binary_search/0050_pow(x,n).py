'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag = 1
        output = 1
        if n < 0:
            flag = -1
            n = -n
        bin_n = str(bin(n))[2:][::-1]
        tmp = x
        for x in bin_n:
            if x == '1': 
                output *= tmp
            tmp = tmp * tmp
        return output if flag == 1 else 1.0 / output