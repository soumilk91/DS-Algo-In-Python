"""
Author: Soumil Ramesh Kulkarni
Date: 01/31/2024

Question:
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates
that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

eg:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
"""

from typing import *
class Solution:
    def dfs(self, source, graph, visited):
        # Change the visited Array
        visited[source] = 1
        # For loop only if the vertex has neighbours
        if source in graph:
            for neighbor in graph[source]:
                # Only if the neighbor is not visited, Recurse
                if visited[neighbor] == 0:
                    self.dfs(neighbor, graph, visited)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build the Graph First
        # We will Use AdjacencyLists
        # Index represents the vertex and the list at that index represents the neighbours
        graph = {}
        # Key in the Graph represents the Vertex and the values represent the neighbours
        for edge in edges:
            if edge[0] in graph:
                graph[(edge[0])].append(edge[1])
            else:
                graph[(edge[0])] = [edge[1]]

            # Because undirected Graph
            if edge[1] in graph:
                graph[(edge[1])].append(edge[0])
            else:
                graph[(edge[1])] = [edge[0]]

        # Now Lets Create a list to track all visited vertices
        visited = [0] * n
        return_count = 0
        # This Return Count will stay at 1 if all the vertices in the Graph are connected
        for i in range(n):
            if visited[i] == 0:
                return_count += 1
                self.dfs(i, graph, visited)

        return return_count