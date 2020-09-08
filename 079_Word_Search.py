'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.board = board
        flag = [[0]*len(board[0]) for i in range(len(board))]
        sums = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                flag[i][j] = 1
                sums += self.dfs([i, j], board[i][j], word, flag)
                flag[i][j] = 0
        
        if sums > 0:
            return True
        else:
            return False
        
    def dfs(self, cur, one_str, word, flag):
        if len(one_str) == len(word):
            if one_str == word:
                return 1
            else:
                return 0
        if one_str != word[:len(one_str)]:
            return 0
        
        for x in self.direction:
            if not self.outside(cur, x, flag):
                flag[cur[0] + x[0]][cur[1] + x[1]] = 1
                if self.dfs([cur[0] + x[0], cur[1] + x[1]], one_str + self.board[cur[0] + x[0]][cur[1] + x[1]], word, flag):
                    return 1
                flag[cur[0] + x[0]][cur[1] + x[1]] = 0
                
        return 0
    
    
    def outside(self, cur, direction, flag):
        if cur[0] + direction[0] >= len(self.board) or cur[0] + direction[0] < 0 or cur[1] + direction[1] >= len(self.board[0]) or cur[1] + direction[1] < 0:
            return True
        elif flag[cur[0] + direction[0]][cur[1] + direction[1]] == 1:
            return True
        else:
            return False
