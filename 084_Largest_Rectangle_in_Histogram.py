'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        heights.append(0)
        for idx, x in enumerate(heights):
            while x < heights[stack[-1]]:
                left = stack.pop()
                max_area = max(max_area, heights[left] * (idx - stack[-1] - 1 ) )
            stack.append(idx)
        return max_area
