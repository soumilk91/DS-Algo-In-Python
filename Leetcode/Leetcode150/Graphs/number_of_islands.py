"""
Author: Soumil Ramesh Kulkarni
Date: 03.18.2024

Question:
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

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

from typing import *
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        numIslands = 0
        # USE Graph BFS
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    numIslands += 1
                    self.graphBFS(grid, row, col)
        return numIslands

    def graphBFS(self, grid, row, col):
        queue = deque([(row, col)])
        while queue:
            currRow, currCol = queue.popleft()
            if 0 <= currRow < len(grid) and 0 <= currCol < len(grid[0]) and grid[currRow][currCol] == '1':
                grid[currRow][currCol] = '2'
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for direction in directions:
                    newRow = currRow + direction[0]
                    newCol = currCol + direction[1]
                    queue.append((newRow, newCol))