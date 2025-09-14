"""
Author: Soumil Ramesh Kulkarni
Date: 03.24.2024

Question:
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1))
such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.



Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
"""

from collections import deque

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        if not grid or not grid[0]:
            return -1
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        queue = deque([])
        visited.add((0, 0))
        queue.append((0, 0, 1))
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        while queue:
            row, col, currentNodes = queue.popleft()
            if row == ROWS - 1 and col == COLS - 1 and grid[row][col] == 0:
                return currentNodes
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                if 0 <= newRow < ROWS and 0 <= newCol < COLS and (newRow, newCol) not in visited and grid[newRow][newCol] == 0:
                    visited.add((newRow, newCol))
                    queue.append((newRow, newCol, currentNodes + 1))
        return -1