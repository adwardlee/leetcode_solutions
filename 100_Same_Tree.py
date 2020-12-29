'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''

### method1 bfs ###
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if q == None and p == None:
            return True
        elif q == None or p == None:
            return False
        stack = [[p,q]]
        while len(stack) != 0:
            a,b = stack.pop()
            if a == None and b == None:
                continue
            elif a == None or b == None:
                return False
            elif a.val != b.val:
                return False
            else:
                stack.append([a.right, b.right])
                stack.append([a.left, b.left])
        return True
 ### method 2 dfs #######
 class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val == q.val:        
            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
        else:
            return False
