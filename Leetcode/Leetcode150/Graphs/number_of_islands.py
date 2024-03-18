"""
Author: Soumil Ramesh Kulkarni
Date: 03.18.2024

Question:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

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


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1':
                    islands += 1
                    self.bfs(grid, row, column)
        return islands

    def bfs(self, matrix, row, column):
        queue = [(row, column)]
        while queue:
            temp = queue.pop(0)
            i = temp[0]
            j = temp[1]
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == '1':
                matrix[i][j] = '2'
                queue.append((i - 1, j))
                queue.append((i + 1, j))
                queue.append((i, j - 1))
                queue.append((i, j + 1))