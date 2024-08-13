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

from collections import deque
from typing import *
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def bfs(r, c):
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            currentArea = 0
            queue = deque([(r, c)])
            visited.add((r, c))
            while queue:
                row, col = queue.popleft()
                currentArea += 1
                for direction in directions:
                    newR, newC = row + direction[0], col + direction[1]
                    if 0 <= newR < ROWS and 0 <= newC < COLS and (newR, newC) not in visited and grid[newR][newC] == 1:
                        visited.add((newR, newC))
                        queue.append((newR, newC))
            return currentArea

        islands = 0
        maxArea = 0
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    islands += 1
                    currentArea = bfs(row, col)
                    maxArea = max(maxArea, currentArea)
        return maxArea
