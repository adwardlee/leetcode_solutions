'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        outstring = '1'
        if n == 1:
            return outstring
        for i in range(n-1):
            count = 1
            outstr = ''
            length = len(outstring)
            for x in range(length-1):
                if outstring[x] == outstring[x+1]:
                    count += 1
                else:
                    outstr = outstr + str(count) + str(outstring[x])
                    count = 1
            outstr = outstr + str(count) + str(outstring[-1])
            outstring = outstr
        return outstring
