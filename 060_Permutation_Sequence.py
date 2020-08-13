'''

'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        inlist = [x for x in range(1, n + 1)]
        multiple = 1
        final_out = []
        m = n
        for i in range(n - 1):
            tmp = factorial(m - 1)
            while k > multiple * tmp:
                multiple += 1
            
            final_out.append(inlist[multiple - 1])
            inlist.remove(inlist[multiple - 1])
            k = k - (multiple - 1) * tmp
            m = m - 1
            multiple = 1
        final_out.append(inlist[0])
        out = ''
        for x in final_out:
            out = out + str(x)
        return out
        
    def factorial(self, x):
        out = x
        while x != 1:
            x = x - 1
            out *= x
        return out
