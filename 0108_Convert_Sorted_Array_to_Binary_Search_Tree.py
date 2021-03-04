'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def subTree(start, end):
            if start >= end:
                return None
            # if len(nums) % 2 == 0:
            root_idx = (start + end) // 2
            # else:
                # root_idx = nums[len(nums) // 2]
            root = TreeNode(nums[root_idx])
            root.left = subTree(start, root_idx)
            root.right = subTree(root_idx + 1, end)
            return root

        return subTree(0, len(nums))