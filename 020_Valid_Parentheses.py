'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicts = {'(':')', '[':']', '{': '}'}
        for x in s:
            if x in dicts.keys():
                stack.append(x)
            elif x in dicts.values():
                for key, values in dicts.items():
                    if x == values:
                        if len(stack) > 0 and stack[-1] == key:
                            stack.pop()
                            break
                        else:
                            return False
            else:
                return False
        if len(stack) > 0:
            return False
        return True