'''
Description
Design an iterator to realize the function of flattening two-dimensional vector.

Example
Example 1:

Input:[[1,2],[3],[4,5,6]]
Output:[1,2,3,4,5,6]
Example 2:

Input:[[7,9],[5]]
Output:[7,9,5]
'''

class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.vec2d = []
        for vec in vec2d:
            for x in vec:
                self.vec2d.append(x)
        self.index = 0

    # @return {int} a next element
    def next(self):
        # Write your code here
        tmp = self.index
        self.index += 1
        return self.vec2d[tmp]

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        if self.index <= len(self.vec2d) - 1:
            return True
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())