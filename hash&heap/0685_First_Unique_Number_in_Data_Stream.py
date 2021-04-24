'''
Description
Given a continuous stream of data, write a function that returns the first unique number (including the last number) when the terminating number arrives. If the terminating number is not found, return -1.

Example
Example1

Input: 
[1, 2, 2, 1, 3, 4, 4, 5, 6]
5
Output: 3
Example2

Input: 
[1, 2, 2, 1, 3, 4, 4, 5, 6]
7
Output: -1
Example3

Input: 
[1, 2, 2, 1, 3, 4]
3
Output: 3
'''

class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        onedict = {}
        flag = False
        for i, x in enumerate(nums):
            if x not in onedict:
                onedict[x] = [1, i]
            else:
                onedict[x][0] += 1
            if number == x:
                flag = True
                break
        if flag == True:
            oncelist = []
            for key in onedict:
                if onedict[key][0] == 1:
                    oncelist.append([key, onedict[key][1]])
            x = 2e30
            returnkey = None
            for one in oncelist:
                if one[1] < x:
                    x = one[1]
                    returnkey = one[0]
            return returnkey
        else:
            return -1