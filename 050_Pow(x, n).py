'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            flag = 1
        else:
            flag = 0
        n = abs(n)
        temp = n
        outlist = []
        while n > 1:
            count = 0
            number = 1
            while temp >= 2:
                temp = temp // 2
                count += 1
                number *= 2
            outlist.append(count)
            n = n - number
            temp = n
        if n == 1:
            outlist.append(0)
        sums = [0 for i in range(outlist[0] + 1)]
        for idx, i in enumerate(range(len(sums))):
            if idx == 0:
                sums[idx] = x
            else:
                sums[idx] = sums[idx - 1] * sums[idx - 1]
        #sums = sums[::-1]
        outsum = 1
        for i in outlist:
            outsum *= sums[i]
        if flag > 0:
            return outsum
        else:
            return 1.0 / outsum
