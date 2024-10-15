"""
Author: Soumil Ramesh Kulkarni
Date: 03.04.2024

Question:
Given an undirected graph, find its total number of connected components.

Example One
Graph

{
"n": 5,
"edges": [[0 ,1], [1, 2], [0, 2], [3, 4]]
}
Output:

2
Example Two
Graph

{
"n": 4,
"edges": [[0 , 1], [0 , 3], [0 , 2], [2 , 1], [2 , 3]]
}
Output:

1
"""

from collections import deque
from typing import *
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n < 1:
            return 0
        if n < 2:
            return 1
        # Build the Graph
        graph = {}
        for node in range(n):
            graph[node] = []
        for edge in edges:
            # Since this is an undirected Graph
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # Treverse the Graph nodes and count the components
        components = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                components += 1
                self.bfs(graph, node, visited)
        return components

    def bfs(self, graph, node, visited):
        queue = deque([])
        queue.append(node)
        while queue:
            currNode = queue.popleft()
            visited.add(currNode)
            for neighbor in graph[currNode]:
                if neighbor not in visited:
                    queue.append(neighbor)