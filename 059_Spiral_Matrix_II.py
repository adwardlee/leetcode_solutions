'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        oldMatrix = [[0] * n for i in range(n)]
        newMatrix = [[0] * n for i in range(n)]
        number = 2
        orient = [0, 0]
        choice = 0
        newMatrix[0][0] = 1
        oldMatrix[0][0] = 1
        for i in range(1, n ** 2):
                orient[0] = orient[0] + direction[choice][0]
                orient[1] = orient[1] + direction[choice][1]
                newMatrix[orient[0]][orient[1]] = number
                oldMatrix[orient[0]][orient[1]] = 1
                if (orient[1] + direction[choice][1]) >= n or (orient[1] + direction[choice][1]) < 0 or (orient[0] + direction[choice][0]) >= n or (orient[0] + direction[choice][0]) < 0 or oldMatrix[orient[0] + direction[choice][0]][orient[1] + direction[choice][1]] == 1:
                    choice += 1
                    choice = choice % 4
                
                number += 1
        return newMatrix
