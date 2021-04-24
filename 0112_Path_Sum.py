'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Example 3:

Input: root = [1,2], targetSum = 0
Output: false
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        self.output = False
        if root == None:
            return False
        self.dfs(targetSum, root)
        return self.output
        
        
    def dfs(self, remain, node):
        if node.left == None and node.right == None and node.val == remain:
            self.output = True
            return True
        elif node.left == None and node.right == None:
            return False
        if node.left != None and self.dfs(remain - node.val, node.left):
            return True
        if node.right != None and self.dfs(remain - node.val, node.right):
            return True
            
        return False 
		
	
	def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        stack = [[[root, 0]]]
        if root == None:
            return False
        while stack:
            tmp = stack.pop()
            onestack = []
            for x, value in tmp:
                if x.left == None and x.right == None:
                    if (x.val + value == targetSum):
                        return True
                if x.left != None:
                    onestack.append([x.left, value + x.val])
                if x.right != None:
                    onestack.append([x.right, value + x.val])
            if onestack != []:
                stack.append(onestack)
                
        return False