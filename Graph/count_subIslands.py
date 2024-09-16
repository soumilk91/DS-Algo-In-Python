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

from typing import *
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # simultaneous Traverse
        ROWS = len(grid2)
        COLS = len(grid2[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid2[r][c] == 0 or (r, c) in visited:
                return True
            visited.add((r, c))
            result = True
            if grid1[r][c] == 0:
                result = False
            result = dfs(r - 1, c) and result
            result = dfs(r + 1, c) and result
            result = dfs(r, c - 1) and result
            result = dfs(r, c + 1) and result
            return result

        visited = set()
        count = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid2[row][col] == 1 and (row, col) not in visited and dfs(row, col):
                    count += 1
        return count

