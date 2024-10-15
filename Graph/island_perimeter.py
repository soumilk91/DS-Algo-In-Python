"""
Author: Soumil Kulkarni
Question:
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.
"""

from typing import *

class Solution1:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        result = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    result += 4

                    if row > 0 and grid[row - 1][col] == 1:
                        result -= 2
                    if col > 0 and grid[row][col - 1] == 1:
                        result -= 2
        return result
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(row, col):
            # Return 1 when we reach the outer bound of the island
            if row >= (len(grid)) or col >= len(grid[0]) or row < 0 or col < 0 or grid[row][col] == 0:
                return 1
            # Base Case to return if the cell is already visited
            if (row, col) in visited:
                return 0

            visited.add((row, col))
            perimeter = dfs(row + 1, col)
            perimeter += dfs(row - 1, col)
            perimeter += dfs(row, col + 1)
            perimeter += dfs(row, col - 1)
            return perimeter

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return dfs(row, col)