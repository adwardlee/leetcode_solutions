'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.output = []
        self.dfs(n, [])
        return self.visualize_matrix(n)
        
    def visualize_matrix(self, n):
        final = []
        matrix = []
        for i in range(n):
            matrix.append('.' * n)
        for x in self.output:
            temp = matrix.copy()
            for idx, y in enumerate(x):
                temp[idx] = temp[idx][:y] + 'Q' + temp[idx][y + 1:]
            final.append(temp)
        return final
        
    def indiagonal(self, x, output):
        ban = []
        row = len(output)
        for idx, num in enumerate(output):
            ban.append(num + row - idx)
            ban.append(num - row + idx)
        if x not in ban:
            return True
        else:
            return False
        
    def dfs(self, n, output):
        if len(output) == n:
            self.output.append(output.copy())
            return
        
        for x in range(n):
            if x not in output and self.indiagonal(x, output):
                self.dfs(n, output + [x])
                
        
        return
