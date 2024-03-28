"""
Author: Soumil Ramesh Kulkarni
Date: 03.26.2024

Question:
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        table = []
        for i in range(numRows):
            table.append([0] * (i + 1))
        print(table)
        # Initialize Base Cases
        table[0][0] = 1
        for i in range(1, numRows):
            table[i][0] = 1
            table[i][-1] = 1
        print(table)
        # Now fill in the triangle.
        # Notice we start from row 2 and col 1 to n - 1
        for row in range(2, numRows):
            for col in range(1, row):
                table[row][col] = table[row - 1][col] + table[row - 1][col - 1]
        print(table)
        return table