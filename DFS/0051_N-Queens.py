'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.output = []
        self.n = n
        matrix = [['.'] * n for i in range(n)]

        self.col_index = []
        col_key = {}
        for i in range(n):
            col_key[i] = 1
        self.onemap = [col_key.copy() for i in range(n)]
        self.backtracking(matrix, 0)
        return self.output

    def backtracking(self, matrix, row):
        if row == self.n:
            out = [''.join(matrix[i]) for i in range(self.n)]
            self.output.append(out)
            return
        x = row
        for y in self.onemap[x].keys():
            matrix[x][y] = 'Q'
            self.col_index.append(y)
            index = self.del_index(x + 1)
            self.backtracking(matrix, x + 1)
            matrix[x][y] = '.'
            self.col_index.pop()
            for one in index:
                self.onemap[x + 1][one] = 1

        return

    def del_index(self, row):
        if row == self.n:
            return []
        out_index = []
        for i in range(0, row):
            col = self.col_index[i]
            cur_col = [col, col - (row - i), col + (row - i)]
            for one in cur_col:
                if one in self.onemap[row]:
                    self.onemap[row].pop(one)
                    out_index.append(one)
        return out_index