'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        self.inorder_index = {x: idx for idx,x in enumerate(inorder)}
        preorder = postorder[::-1]


        def buildSubTree(start, end, start_in, end_in):
            if start >= end or start_in >= end_in:
                return None
            root_node = preorder[start]
            root_index = self.inorder_index[root_node]
            length = end_in - root_index
            root = TreeNode(root_node)
            left = buildSubTree(start + length, end, start_in, root_index)
            right = buildSubTree(start + 1, start + length, root_index + 1, end_in)
            root.left = left
            root.right = right
            return root

        return buildSubTree(0, len(preorder), 0, len(inorder))
