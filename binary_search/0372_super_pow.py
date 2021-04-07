'''
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

 

Example 1:

Input: a = 2, b = [3]
Output: 8
Example 2:

Input: a = 2, b = [1,0]
Output: 1024
Example 3:

Input: a = 1, b = [4,3,3,8,5,2]
Output: 1
Example 4:

Input: a = 2147483647, b = [2,0,0]
Output: 1198
 

Constraints:

1 <= a <= 231 - 1
1 <= b.length <= 2000
0 <= b[i] <= 9
b doesn't contain leading zeros.
'''


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        a = a % 1337
        length = len(b)
        basis = a
        result = 1
        for i in range(length - 1, -1, -1):
            output = self.powResult(basis, 10)
            result = (result * output[b[i]]) % 1337
            basis = output[10]
        return result
            
    def powResult(self, x, y):
        output = [1]
        result = 1
        for i in range(y):
            result = (result * x ) % 1337
            output.append(result)
        return output
            