'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        alls = []
        stack = [[[root, 0, []]]]
        if root == None:
            return []
        while stack:
            tmp = stack.pop()
            onestack = []
            for x, value, onelist in tmp:
                if x.left == None and x.right == None:
                    if (x.val + value == targetSum):
                        alls.append(onelist + [x.val])
                if x.left != None:
                    onestack.append([x.left, value + x.val, onelist + [x.val]])
                if x.right != None:
                    onestack.append([x.right, value + x.val, onelist + [x.val]])
            if onestack != []:
                stack.append(onestack)

        return alls