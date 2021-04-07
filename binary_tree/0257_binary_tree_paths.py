'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = []
        self.onePath(root, str(root.val))
        return self.paths
        
    def onePath(self, root, path):
        if root.left == None and root.right == None:
            self.paths.append(path)
        if root.left:
            self.onePath(root.left, path + '->' + str(root.left.val))
        if root.right:
            self.onePath(root.right, path + '->' + str(root.right.val))
            
###  time complexity : O(n)
###  space complexity: O(n)
#### DFS traverse all nodes