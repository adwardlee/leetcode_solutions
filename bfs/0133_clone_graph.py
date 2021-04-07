'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_to_neighbors = {}
        newnode_to_neighbors = {}
        if node == None:
            return None
        listnode = deque([node])
        output = []
        while listnode:
            firstnode = listnode.popleft()
            if firstnode.val not in node_to_neighbors:
                node_to_neighbors[firstnode.val] = firstnode.neighbors
            for x in firstnode.neighbors:
                if x.val not in node_to_neighbors:
                    node_to_neighbors[x.val] = x.neighbors
                    listnode.append(x)
        for idx, key in enumerate(node_to_neighbors):
            
            if key not in newnode_to_neighbors:
                
                tmp = Node(val=key,neighbors=[])
                newnode_to_neighbors[key] = tmp
                if idx == 0:
                    output = tmp
            else:
                tmp = newnode_to_neighbors[key]
            for x in node_to_neighbors[key]:
                if x.val not in newnode_to_neighbors:
                    tmpneighbor = Node(val=x.val, neighbors=[])
                    newnode_to_neighbors[x.val] = tmpneighbor
                else:
                    tmpneighbor = newnode_to_neighbors[x.val]
                if tmpneighbor not in tmp.neighbors:
                    tmp.neighbors.append(tmpneighbor)
        return output

        