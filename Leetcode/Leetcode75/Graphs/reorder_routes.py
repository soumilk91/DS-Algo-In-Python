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
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for connection in connections:
            graph[connection[0]].append([connection[1], 1])
            graph[connection[1]].append([connection[0], -1])
        visited = set()
        minChange = [0]
        self.dfs(graph, visited, minChange, 0)
        return minChange[0]

    def dfs(self, graph, visited, minChange, currCity):
        visited.add(currCity)
        for neighborCity in graph[currCity]:
            if neighborCity[0] not in visited:
                if neighborCity[1] == 1:
                    minChange[0] += 1
                self.dfs(graph, visited, minChange, neighborCity[0])