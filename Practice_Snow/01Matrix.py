"""
Author: Soumil Ramesh Kulkarni
Date: 05.07.2024

Question:
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
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        matrix = [row[:] for row in mat]
        queue = deque([])
        seen = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    queue.append((row, col, 0))
                    seen.add((row, col))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, step = queue.popleft()
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (new_row, new_col) not in seen and 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, step + 1))
                    matrix[new_row][new_col] = step + 1
        return matrix
