'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.opts = 0
        self.dfs(n, [])
        return self.opts
    
    def dfs(self,n, output):
        if len(output) == n:
            self.opts += 1
            return 
        
        for x in range(n):
            if x in output or self.isdiagonal(output, x):
                continue
            else:
                self.dfs(n, output + [x])
                
        return
        
    def isdiagonal(self, output, x):
        exists = []
        s = len(output)
        for idx, i in enumerate(output):
            exists.append(i + s - idx)
            exists.append(i - s + idx)
        if x in exists:
            return True
        else:
            return False
