'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        one_length = sqrt(length)
        rows = [[] for x in range(length)]
        cols = [[] for x in range(length)]
        blocks = [[] for x in range(length)]
        for i in range(length):
            for j in range(length):
                if board[i][j] != '.':
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in blocks[int(j * one_length // length + i // one_length * one_length)]:
                        return False
                    rows[i].append(board[i][j])
                    cols[j].append(board[i][j])
                    blocks[int(j * one_length // length + i // one_length * one_length)].append(board[i][j])
                    
        return True
