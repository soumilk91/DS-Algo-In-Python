"""
Question:

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell
is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4

"""
from typing import *
from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(row, col):
            currPeri = 0
            queue = deque([(row, col)])
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            while queue:
                r, c = queue.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                for x, y in directions:
                    newR, newC = r + x, c + y
                    if 0 <= newR < ROWS and 0 <= newC < COLS:
                        if grid[newR][newC] == 0:
                            currPeri += 1
                        if grid[newR][newC] == 1:
                            queue.append((newR, newC))
                    else:
                        currPeri += 1
            return currPeri

        maxPeri = 0
        visited = set()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    currPeri = bfs(row, col)
                    maxPeri = max(currPeri, maxPeri)
        return maxPeri