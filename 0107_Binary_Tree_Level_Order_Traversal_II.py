'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        stack = [[root]]
        res = []
        while stack:
            onelist = stack.pop()
            oneres = []
            onestack = []
            for x in onelist:
                if x.left != None:
                    onestack.append(x.left)
                if x.right != None:
                    onestack.append(x.right)
                oneres.append(x.val)
            if onestack != []:
                stack.append(onestack)
            if oneres != []:
                res.append(oneres)
        return res[::-1]
        
