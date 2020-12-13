'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0
 

Constraints:

rows == matrix.length
cols == matrix.length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        elif len(matrix[0]) == 0:
            return 0
        height = [[0] * (len(matrix[0]) + 1)] *len(matrix)
        max_area = 0
        for i in range(len(matrix)):
            stack = [-1]
            left = 0
            for j in range(len(matrix[0]) + 1):
                if j < len(matrix[0]):
                    height[i][j] = height[i - 1][j] * int(matrix[i][j]) + int(matrix[i][j])
                if i == 0 and j < len(matrix[0]):
                    height[i][j] = int(matrix[i][j])
                while height[i][stack[-1]] > height[i][j]:
                    max_area = max(max_area, (j - stack[-2] - 1) * height[i][stack[-1]])
                    stack.pop()
                    
                    
                stack.append(j)
                
        return max_area
        
            
