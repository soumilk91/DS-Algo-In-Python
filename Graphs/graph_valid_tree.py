"""
Author: Soumil Ramesh Kulkarni
Date: 01/31/2024

Question: You have a graph of n nodes labeled from 0 to n - 1.
You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that
there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Eg:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
"""


# A tree is basically a connected Graph Without Cycles
# Detecting a cycle is basically detecting if there are any cross edges
# While Traversing, if the neighbor of any node is already visited and that node is not the parent of the current node,
# then it is a cross Edge
class Solution:
    def dfs(self, source, graph, visited, parent):
        visited[source] = 1
        if source in graph:
            for neighbor in graph[source]:
                if visited[neighbor] == -1:
                    parent[neighbor] = source
                    if self.dfs(neighbor, graph, visited, parent):
                        return True
                else:
                    if neighbor != parent[source]:
                        return True
            return False

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Build a Graph
        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])

            if edge[1] not in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])

        visited = [-1] * n
        parent = [1] * n
        component = 0

        for i in range(n):
            if visited[i] == -1:
                component += 1
                if component > 1:
                    return False
                if self.dfs(i, graph, visited, parent):
                    return False
        return True
