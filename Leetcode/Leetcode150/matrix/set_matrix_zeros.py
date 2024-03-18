"""
Author: Soumil Ramesh Kulkarni
Date: 03.18.2024

Question:
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        initial_zeros_rows = {}
        initial_zeros_colum = {}
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    initial_zeros_rows[row] = 1
                    initial_zeros_colum[column] = 1
        # print(initial_zeros)

        # Make another pass
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if row in initial_zeros_rows or column in initial_zeros_colum:
                    matrix[row][column] = 0