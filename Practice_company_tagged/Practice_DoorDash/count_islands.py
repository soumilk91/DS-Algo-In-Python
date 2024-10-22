"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from collections import deque
from typing import *
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    visited.add((row, col))
                    islands += 1
                    self.bfs(grid, row, col, visited)
        return islands

    def bfs(self, grid, row, col, visited):
        queue = deque([])
        queue.append((row, col))
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            row, col = queue.popleft()
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and (newRow, newCol) not in visited and \
                        grid[newRow][newCol] == "1":
                    visited.add((newRow, newCol))
                    queue.append((newRow, newCol))