"""
Question:
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

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
        if not grid:
            return 0

        def bfs(row, col):
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            queue = deque([(row, col)])
            visited.add((row, col))
            currArea = 1
            while queue:
                r, c = queue.popleft()
                for direction in directions:
                    newR, newC = r + direction[0], c + direction[1]
                    if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == 1 and (
                    newR, newC) not in visited:
                        visited.add((newR, newC))
                        queue.append((newR, newC))
                        currArea += 1
            return currArea

        maxArea = 0
        islands = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    currArea = bfs(row, col)
                    islands += 1
                    maxArea = max(maxArea, currArea)
        return maxArea