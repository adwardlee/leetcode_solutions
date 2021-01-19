'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        self.inorder_index = {x: idx for idx,x in enumerate(inorder)}


        def buildSubTree(start, end, start_in, end_in):
            if start >= end or start_in >= end_in:
                return None
            root_node = preorder[start]
            root_index = self.inorder_index[root_node]
            length = root_index - start_in
            root = TreeNode(root_node)
            left = buildSubTree(start + 1, start + length + 1, start_in, root_index)
            right = buildSubTree(start + length + 1, end, root_index + 1, end_in)
            root.left = left
            root.right = right
            return root

        return buildSubTree(0, len(preorder), 0, len(inorder))
