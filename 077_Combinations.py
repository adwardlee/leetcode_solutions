'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.output = []
        self.subsets(1, n + 1, k, [])
        return self.output
    
    def subsets(self, start, n, k, cur):
        if len(cur) == k:
            self.output.append(cur.copy())
            return 
        for i in range(start, n):
            cur.append(i)
            self.subsets(i + 1, n, k, cur)
            cur.pop()
        return
