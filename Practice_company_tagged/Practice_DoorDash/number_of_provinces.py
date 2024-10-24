"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected,
and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

"""

from typing import *
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Create a Graph
        graph = {city: set() for city in range(len(isConnected))}
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1:
                    if row != col:
                        graph[row].add(col)
                        graph[col].add(row)
        # print(graph)
        provinces = 0
        visited = set()

        for city in range(len(isConnected)):
            if city not in visited:
                provinces += 1
                self.bfs(graph, city, visited)
        return provinces

    def bfs(self, graph, city, visited):
        queue = deque([])
        queue.append(city)
        visited.add(city)
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
