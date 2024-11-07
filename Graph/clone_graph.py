"""
Author: Soumil Kulkarni

Question:
Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.
The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists,
used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph.
The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.
"""

from collections import deque
from typing import *
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_dict = {}
        node_dict[node] = Node(node.val, [])
        queue = deque([node])
        while queue:
            currNode = queue.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in node_dict:
                    node_dict[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                node_dict[currNode].neighbors.append(node_dict[neighbor])
        return node_dict[node]