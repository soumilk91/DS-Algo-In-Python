"""
Author: Soumil Ramesh Kulkarni
Date: 03.30.2024

Question:
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two
different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one
direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.



Example 1:


Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 2:


Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
"""


class Solution:
    def dfs(self, adj: List[List[Tuple[int, int]]], visited: List[bool], minChange: List[int], currCity: int) -> None:
        visited[currCity] = True
        for neighbourCity in adj[currCity]:
            if not visited[neighbourCity[0]]:
                if neighbourCity[1] == 1:
                    minChange[0] += 1
                self.dfs(adj, visited, minChange, neighbourCity[0])

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append((connection[1], 1))
            adj[connection[1]].append((connection[0], -1))
        visited = [False] * n
        minChange = [0]
        self.dfs(adj, visited, minChange, 0)
        return minChange[0]