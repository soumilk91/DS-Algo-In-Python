"""
Author: Soumil Kulkarni

Question:
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water.
You may assume water is surrounding the grid (i.e., all the edges are water).

Example:

Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1


Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4
"""

from collections import deque
from typing import *
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    visited.add((row, col))
                    islands += 1
                    self.bfs(grid, row, col, visited)
        return islands

    def bfs(self, grid, row, col, visited):
        queue = deque([])
        queue.append((row, col))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            for direction in directions:
                newRow, newCol = r + direction[0], c + direction[1]
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] == "1" and (
                newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    queue.append((newRow, newCol))
