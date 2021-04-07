'''
Description
Please design a data structure which can do the following operations:

void addEdge(int a, int b):add an edge between node aa and node bb. It is guaranteed that there isn't self-loop or multi-edge.
bool isValidTree(): Check whether these edges make up a valid tree.
 
Example
Example 1

Input:
addEdge(1, 2)
isValidTree()
addEdge(1, 3)
isValidTree()
addEdge(1, 5)
isValidTree()
addEdge(3, 5)
isValidTree()
Output: ["true","true","true","false"]

'''

from collections import deque
class Solution:
    """
    @param a: the node a
    @param b: the node b
    @return: nothing
    """
    def __init__(self):
        self.graph = []

    def addEdge(self, a, b):
        # write your code here
        if [a,b] or [b,a] not in self.graph:
            self.graph.append([a,b])
    """
    @return: check whether these edges make up a valid tree
    """
    def isValidTree(self):
        # write your code here
        graphlist = {}
        graphdict = {}
        visited = {}
        edges = 0
        for edge in self.graph:
            if edge[0] not in graphlist:
                visited[edge[0]] = 0
                graphlist[edge[0]] = []
                graphdict[edge[0]] = 1
            else:
                graphdict[edge[0]] += 1
            graphlist[edge[0]].append(edge[1])
            if edge[1] not in graphlist:
                visited[edge[1]] = 0
                graphlist[edge[1]] = []
                graphdict[edge[1]] = 1
            else:
                graphdict[edge[1]] += 1
            graphlist[edge[1]].append(edge[0])
            edges += 1
        if len(graphlist) != edges + 1:
            return False
        queue = deque()
        for key in graphlist:
            if len(graphlist[key]) == 1:
                queue.append(key)
                visited[key] = 1
        
        length = len(graphlist.keys())
        count = 0
        while queue:
            front = queue.popleft()
            count += 1
            for x in graphlist[front]:
                graphdict[x] -= 1
                if graphdict[x] <= 1 and not visited[x]:
                    queue.append(x)
                    visited[x] = 1
        return count == length