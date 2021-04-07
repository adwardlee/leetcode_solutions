'''
Description
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

You can assume that there is at least one topological order in the graph.


Example
For graph as follow:


The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
Challenge
Can you do it in both BFS and DFS?
'''

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        graphdict = {}
        graphcount = {}
        output = []
        for x in graph:
            graphdict[x] = []
            if x not in graphcount:
                graphcount[x] = 0
            for y in x.neighbors:
                graphdict[x].append(y)
                if y not in graphcount:
                    graphcount[y] = 1
                else:
                    graphcount[y] += 1
        queue = deque()
        for key in graphcount:
            if graphcount[key] == 0:
                queue.append(key)
        while queue:
            node = queue.popleft()
            output.append(node)
            for nextnode in graphdict[node]:
                graphcount[nextnode] -= 1
                if graphcount[nextnode] == 0:
                    queue.append(nextnode)
        return output