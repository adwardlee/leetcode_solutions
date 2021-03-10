'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = [[0] * self.cols for row in range(self.rows)]
        number = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.visited[i][j] and grid[i][j] == '1':
                    number += 1
                    self.visited[i][j] = 1
                    self.traverseNode(j, i, grid)
                
        return number
            
    def traverseNode(self, x, y, grid):
        move = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        tmp = deque([(x ,y )])
        while tmp:
            tmp_node = tmp.popleft()
            for step in move:
                if self.isvalid(tmp_node[0] + step[0], tmp_node[1] + step[1], grid):
                    tmp.append((tmp_node[0] + step[0], tmp_node[1] + step[1]))
                    self.visited[tmp_node[1] + step[1]][tmp_node[0] + step[0]] = 1
        return
        
    def isvalid(self, x, y, grid):
        if (x > -1) and (x < self.cols) and (y > -1) and (y < self.rows) and (self.visited[y][x] == 0) and grid[y][x] == '1':
            return True
        else:
            return False