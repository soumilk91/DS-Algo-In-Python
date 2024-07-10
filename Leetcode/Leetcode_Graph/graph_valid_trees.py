"""
Question:
ou have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges
where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.



Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
"""

from typing import *
from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Base Case when the Graph has less than 2 nodes
        if n < 2:
            return True
        # Graph is valid Tree if there exists no Loop in the Graph
        # Build the Graph First and do a Traverse ...
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # Traverse ... If edge not visited or edge is parent ... Allowed ... else Loop Present
        # Using BFS

        queue = deque([0])
        parent = {0: None}
        visited = set()
        visited.add(0)
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in visited:
                    if parent[node] == neighbor:
                        continue
                    else:
                        # Cycle exists
                        return False
                else:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
        # If graph is not connected ... Basically has more components than 1
        if len(visited) != n:
            return False
        return True