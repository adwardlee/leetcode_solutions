'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        if cols == 0:
            return False
        row = -1
        for i in range(rows - 1):
            if target > matrix[i][0] and target < matrix[i + 1][0]:
                row = i
                break
            elif target == matrix[i][0] or target == matrix[i + 1][0]:
                return True
        if row == -1:
            if target > matrix[rows - 1][0] and target < matrix[rows - 1][-1]:
                row = rows - 1
            elif target > matrix[rows - 1][-1]:
                return False
            elif target < matrix[0][0]:
                return False
        return self.midSearch(matrix, target, 0, cols - 1, row)
        
        
    def midSearch(self, matrix, value, left, right, row):
        if value > matrix[row][-1]:
            return False
        while left <= right:
            mid = ( left + right ) // 2
            if matrix[row][mid] == value:
                return True
            if matrix[row][mid] > value:
                right = mid - 1
            else:
                left = mid + 1
            
        return False
