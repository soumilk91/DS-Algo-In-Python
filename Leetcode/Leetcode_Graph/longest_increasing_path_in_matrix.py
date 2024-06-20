"""
Question:
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).



Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
"""

# TLE Approach without using memoization
from typing import *
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        maxPath = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                maxPath = max(maxPath, self.bfs(row, col, matrix))
        return maxPath

    def bfs(self, row, col, matrix):
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        from collections import deque
        currPath = 0
        queue = deque([(row, col, 1)])
        while queue:
            r, c, p = queue.popleft()
            currPath = max(currPath, p)
            for direction in directions:
                newRow = r + direction[0]
                newCol = c + direction[1]
                if 0 <= newRow < len(matrix) and 0 <= newCol < len(matrix[0]) and matrix[newRow][newCol] > matrix[r][c]:
                    queue.append((newRow, newCol, p + 1))
        return currPath


