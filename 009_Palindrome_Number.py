'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if y == y[::-1]:
            return True
        else:
            return False
            
            
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = 0
        count = 1
        a = x
        while a != 0:
            temp = a%10
            a = a // 10
            y = 10 * y + temp

        if y == x:
            return True
        else:
            return False
