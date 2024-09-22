"""
Author: Soumil Ramesh Kulkarni
Date: 03.16.2024

Question:
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) # Initial possible number of steps
        direction = 1 # Start off going right
        i, j = 0, -1
        output = []
        while m*n > 0:
            for _ in range(n): # move horizontally
                j += direction
                output.append(matrix[i][j])
            m-= 1
            for _ in range(m): # move vertically
                i += direction
                output.append(matrix[i][j])
            n-=1
            direction *= -1 # flip direction
        return output