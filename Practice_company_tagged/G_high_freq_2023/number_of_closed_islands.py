"""
Author: Soumil Ramesh Kulkarni
Date: 03.25.2024

Question:
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.



Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
"""


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    q = [(i, j)]
                    f = 1
                    while q:
                        ni, nj = q.pop(0)
                        if grid[ni][nj]: continue
                        if ni == 0 or ni == m - 1 or nj == 0 or nj == n - 1: f = 0
                        grid[ni][nj] = 1
                        if ni > 0 and not grid[ni - 1][nj]: q.append((ni - 1, nj))
                        if ni < m - 1 and not grid[ni + 1][nj]: q.append((ni + 1, nj))
                        if nj > 0 and not grid[ni][nj - 1]: q.append((ni, nj - 1))
                        if nj < n - 1 and not grid[ni][nj + 1]: q.append((ni, nj + 1))
                    if f: ans += 1
        return ans