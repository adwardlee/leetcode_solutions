'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

样例
Example 1:

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
Example 2:

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
注意事项
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''

from collections import defaultdict,deque
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False
        if len(edges) == 0:
            return n == 1
        neighbor = defaultdict()
        for edge in edges:
            if edge[0] not in neighbor:
                neighbor[edge[0]] = 1
            else:
                neighbor[edge[0]] += 1
            if edge[1] not in neighbor:
                neighbor[edge[1]] = 1
            else:
                neighbor[edge[1]] += 1
        queue = deque()
        for x in range(n):
            if x not in neighbor:
                return False
            elif neighbor[x] == 1:
                neighbor[x] -= 1
                queue.append(x)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for edge in edges:
                if node in edge:
                    neighbor[edge[0]] -= 1
                    neighbor[edge[1]] -= 1
            if len(queue) == 0:
                for key in neighbor:
                    if neighbor[key] == 1 or neighbor[key] == 0:
                        queue.append(key)
        if count < n:
            return False
        return True