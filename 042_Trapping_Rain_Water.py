'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        width = len(height)
        if width <= 2:
            return 0
        max_h = max(height)
        area = width * max_h
        index = height.index(max_h)
        sums = 0
        left_height = 0
        for i in range(index):
            if height[i] > left_height:
                left_height = height[i]
            sums += (max_h - left_height)
        left_height = 0
        for i in range(width - 1, index - 1, -1):
            if height[i] > left_height:
                left_height = height[i]
            sums += (max_h - left_height)
        for i in range(width):
            sums += height[i]
        return area - sums
