'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

1 <= n <= 19
'''
class Solution:
    def numTrees(self, n: int) -> int:
        self.count = 0
        self.alls = {}
        self.alls[0] = 1
        self.alls[1] = 1
        for i in range(0, n):
            self.alls[i] = self.countTrees(i)
        for i in range(1, n + 1):
            leftTrees = self.alls[i - 1]
            rightTrees = self.alls[n - i]
            self.count += leftTrees * rightTrees
        return self.count
    
    def countTrees(self, a):
        one = 0
        if a <= 0:
            return 1
        if a in self.alls:
            return self.alls[a]
        else:
            for i in range(1, a + 1):
                leftTrees = self.countTrees(i - 1)
                rightTrees = self.countTrees(a - i)
                one += leftTrees * rightTrees
            self.alls[a] = one
        return one
