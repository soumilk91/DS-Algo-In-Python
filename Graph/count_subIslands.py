"""
Author: Soumil Kulkarni
Date: 08.14.2024

Question:

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land).
An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered
water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up
this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Example:
Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
"""

from collections import deque
from typing import *
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid2 or not grid2[0]:
            return 0
        ROWS, COLS = len(grid2), len(grid2[0])
        visited = set()
        subislands = 0

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid2[row][col] == 1:
                    if self.bfs(grid1, grid2, row, col, visited):
                        subislands += 1

        return subislands

    def bfs(self, grid1, grid2, row, col, visited):
        queue = deque([(row, col)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited.add((row, col))
        is_sub_island = True

        while queue:
            currRow, currCol = queue.popleft()

            if grid1[currRow][currCol] != 1:
                is_sub_island = False

            for direction in directions:
                newRow, newCol = currRow + direction[0], currCol + direction[1]
                if 0 <= newRow < len(grid2) and 0 <= newCol < len(grid2[0]) and grid2[newRow][newCol] == 1 and (
                newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    queue.append((newRow, newCol))

        return is_sub_island

