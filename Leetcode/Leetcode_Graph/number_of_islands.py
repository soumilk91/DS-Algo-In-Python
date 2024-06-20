"""
Question:

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.



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
        if not grid:
            return 0
        visited = set()

        def bfs(row, col):
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            queue = deque([(row, col)])
            visited.add((row, col))
            while queue:
                r, c = queue.popleft()
                for direction in directions:
                    newR, newC = r + direction[0], c + direction[1]
                    if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == "1" and (
                    newR, newC) not in visited:
                        queue.append((newR, newC))
                        visited.add((newR, newC))

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    bfs(row, col)
        return islands