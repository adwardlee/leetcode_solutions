'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


'''

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.length = len(board)
        self.row = [[] for x in range(self.length)]
        self.col = [[] for x in range(self.length)]
        self.block = [[] for x in range(self.length)]
        self.board = board
        for i in range(self.length):
            for j in range(self.length):
                if board[i][j] != '.':
                    self.row[i].append(board[i][j])
                    self.col[j].append(board[i][j])
                    self.block[i // 3 * 3 + j // 3].append(board[i][j])
        self.recursion(0, 0)
        return self.board

    def recursion(self, i, j):
        if i == self.length and j == 0:
            return True
        if self.board[i][j] == '.':
            for x in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                self.board[i][j] = x
                if self.isValid(self.board[i][j], i, j):
                    self.row[i].append(x)
                    self.col[j].append(x)
                    self.block[i // 3 * 3 + j // 3].append(x)
                    next_i = i + (j + 1) // self.length
                    next_j = (j + 1) % self.length
                    if self.recursion(next_i, next_j):
                        return True
                    self.row[i].pop()
                    self.col[j].pop()
                    self.block[i // 3 * 3 + j // 3].pop()
                self.board[i][j] = '.'



        else:
            next_i = i + (j + 1) // self.length
            next_j = (j + 1) % self.length
            if self.recursion(next_i, next_j):
                return True

    def isValid(self, number, i, j):
        if number in self.row[i] or number in self.col[j] or number in self.block[i // 3 * 3 + j // 3]:
            return False
        else:
            return True
