'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

Constraints:

1 <= n <= 1690
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 0:
            return None
        result = []
        duplicate = set()
        final = []
        heapq.heappush(result,1)
        count = 0
        while count < n:
            minvalue = heapq.heappop(result)
            final.append(minvalue)
            count += 1
            for i in [2, 3, 5]:
                tmp = i * minvalue
                if tmp not in duplicate:
                    heapq.heappush(result, tmp)
                    duplicate.add(tmp)
        return final[n - 1]