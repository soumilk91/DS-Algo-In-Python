"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

from typing import *
from collections import deque

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        visited = set()

        queue = deque([])
        # Insert all zeros from the matrix in the queue with a distance 0 and add them in the seen set
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    visited.add((row, col))
                    queue.append((row, col, 0))

        # BSF until the queue is empty
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            row, col, currDistance = queue.popleft()
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                if 0 <= newRow < ROWS and 0 <= newCol < COLS and (newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    queue.append((newRow, newCol, currDistance + 1))
                    matrix[newRow][newCol] = currDistance + 1
        return matrix
