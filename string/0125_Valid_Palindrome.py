'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        
        tmp = ''
        for x in s:
            if x.isalpha():
                tmp += x.lower()
            elif x.isnumeric():
                tmp += x
        self.length = len(tmp)
        if self.length == 1 or self.length == 0:
            return True
        elif self.length % 2 == 0:
            return self.checkSubstr(tmp, self.length // 2 - 1, self.length // 2)
        else:
            return self.checkSubstr(tmp, self.length // 2 - 1, self.length // 2 + 1)
        
    def checkSubstr(self, s, left, right):
        while left >= 0 and right <= self.length - 1:
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                return False
        if right - left == self.length + 1:
            return True
        else:
            return False

'''
1. two pointers from start and end to middle
2. from middle to 
'''


'''
Time complexity: O(n)
Space complexity: O(n)
'''