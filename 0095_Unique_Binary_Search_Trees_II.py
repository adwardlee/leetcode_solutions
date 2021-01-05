'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

0 <= n <= 8
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        self.final = []
        for i in range(1, n + 1):
            oneleft = self.generateSubtree(1, i)
            oneright = self.generateSubtree(i + 1, n + 1)
            for left in oneleft:
                for right in oneright:
                    tmp = TreeNode(i)
                    tmp.left = left
                    tmp.right = right
                    self.final.append(tmp)

        return self.final

    def generateSubtree(self, start, end):
        one = []
        if start >= end:
            return [None]
        for i in range(start, end):
            oneleft = self.generateSubtree(start, i)
            oneright = self.generateSubtree(i + 1, end)
            for left in oneleft:
                for right in oneright:
                    tmp = TreeNode(i)
                    tmp.left = left
                    tmp.right = right
                    one.append(tmp)

        return one
