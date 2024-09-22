"""
Author: Soumil Ramesh Kulkarni
Date: 03.16.2024

Question:
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are
directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        n = len(isConnected)
        visited = set()
        count = 0

        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                visited.add(i)
                self.dfs(i, isConnected, visited)
        return count

    def dfs(self, node, isConnected, visited):
        for j in range(len(isConnected)):
            if isConnected[node][j] and j not in visited:
                visited.add(j)
                self.dfs(j, isConnected, visited)