"""
Author: Soumil Kulkarni

Question:
You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically.
You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.

Example:
Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

Output: 6
"""

from typing import *
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        maxArea = 0
        islands = 0
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    currArea = self.bfs(grid, row, col, visited)
                    maxArea = max(maxArea, currArea)
                    islands += 1
        return maxArea

    def bfs(self, grid, row, col, visited):
        queue = deque([])
        queue.append((row, col))
        visited.add((row, col))
        currArea = 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            currRow, currCol = queue.popleft()
            for direction in directions:
                newRow, newCol = currRow + direction[0], currCol + direction[1]
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] == 1 and (
                newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    queue.append((newRow, newCol))
                    currArea += 1
        return currArea

