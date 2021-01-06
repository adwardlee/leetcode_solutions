'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
iterative
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [[root]]
        while stack:
            a = stack.pop()
            oneline = []
            values = []
            for x in a:
                if x != None:
                    oneline.append(x.left)
                    oneline.append(x.right)
                    values.append(x.val)
                else:
                    values.append(None)
            if len(oneline) > 0:
                stack.append(oneline)
            if values != values[::-1]:
                 return False
        return True
'''
recursive
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.checkTree(root, root)
        
    def checkTree(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        else:
            return left.val == right.val and self.checkTree(left.left, right.right) and self.checkTree(left.right, right.left)
