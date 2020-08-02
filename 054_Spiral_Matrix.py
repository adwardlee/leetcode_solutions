'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        index = (0, 0)
        rows = len(matrix)
        if rows < 1:
            return matrix
        elif rows == 1:
            return matrix[0]
        cols = len(matrix[0])
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        output = []
        exists = [[0] *  cols for x in range(rows)]
        count = 0
        all_num = 0
        while all_num < rows * cols:
            all_num += 1
            if index[0] > rows - 1 or index[0] < 0 or index[1] > cols - 1 or index[1] < 0 or exists[index[0]][index[1]] == 1:
                index = (index[0] - direction[count][0], index[1] - direction[count][1])
                count = (count + 1 ) % 4
                all_num -= 1
                
            else:
                output.append(matrix[index[0]][index[1]])
                exists[index[0]][index[1]] = 1
            index = (index[0] + direction[count][0], index[1] + direction[count][1])
        return output
