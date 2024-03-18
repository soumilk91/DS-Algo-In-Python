"""
Author: Soumil Ramesh Kulkarni
Date: 03.16.2024

Question:
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

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
        visited = [False] * n

        def dfs(node):
            for j in range(n):
                if isConnected[node][j] == 1 and visited[j] == False:
                    visited[j] = True
                    dfs(j)

        count = 0
        for i in range(n):
            if visited[i] == False:
                count += 1
                visited[i] = True
                dfs(i)
        return count