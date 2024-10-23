"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""

from collections import deque
from typing import *

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        maxArea = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    visited.add((row, col))
                    currArea = self.bfs(grid, row, col, visited)
                    maxArea = max(maxArea, currArea)
        return maxArea

    def bfs(self, grid, row, col, visited):
        queue = deque([])
        queue.append((row, col))
        currArea = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            row, col = queue.popleft()
            currArea += 1
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and (newRow, newCol) not in visited and \
                        grid[newRow][newCol] == 1:
                    visited.add((newRow, newCol))
                    queue.append((newRow, newCol))
        return currArea
