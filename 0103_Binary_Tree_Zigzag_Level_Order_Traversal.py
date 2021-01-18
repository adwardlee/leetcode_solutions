'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        stack = [[root]]
        count = 0
        res = []
        while stack:
            onelist = stack.pop()
            oneres = []
            onetempstack = []
            for x in onelist:
                if x.left != None:
                    onetempstack.append(x.left)
                if x.right != None:
                    onetempstack.append(x.right)
                oneres.append(x.val)
            if oneres != []:
                if count % 2 == 1:
                    oneres = oneres[::-1] 
                res.append(oneres)
            if onetempstack != []:
                stack.append(onetempstack)
            count += 1

        return res
