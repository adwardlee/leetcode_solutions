'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        stack = [[root]]
        self.final = []
        while stack:
            cur_list = []
            onelist = stack.pop()
            tmp_list = []
            for x in onelist:
                if x != None:
                    tmp_list.append(x.val)
                    if x.left != None:
                        cur_list.append(x.left)
                    if x.right != None:
                        cur_list.append(x.right)
            if len(cur_list) > 0:
                stack.append(cur_list)
            if len(tmp_list) > 0:
                self.final.append(tmp_list)
        return self.final
