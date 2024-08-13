"""
Author: Soumil Ramesh Kulkarni
Date: 03.30.2024

Question:
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

from typing import *
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in range(ROWS):
            for col in range(COLS):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0

        print(matrix)

client = Solution()
print(client.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))