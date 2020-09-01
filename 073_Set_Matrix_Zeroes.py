class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        indexes = [set(), set()]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    indexes[0].add(i)
                    indexes[1].add(j)
        for row in indexes[0]:
            for i in range(cols):
                matrix[row][i] = 0
        for col in indexes[1]:
            for i in range(rows):
                matrix[i][col] = 0
        return matrix
        
