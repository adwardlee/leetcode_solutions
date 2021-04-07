'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_index = self.binarySearch(matrix, target, flag=False)
        if row_index == -1:
            return False
        col_index = self.binarySearch(matrix[row_index], target, flag=True)
        if col_index == -1:
            return False
        return True
        
    
    def binarySearch(self, array, target, flag):
        n = len(array)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if array[mid] == target:
                return mid
            if flag:
                if array[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if array[mid][0] == target or array[mid][-1] == target or (array[mid][0] < target and array[mid][-1] > target):
                    return mid
                elif array[mid][0] > target:
                    right = mid - 1
                elif array[mid][-1] < target:
                    left = mid + 1
                    
        return -1