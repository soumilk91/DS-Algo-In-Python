"""
Author: Soumil Ramesh Kulkarni
Date: 03.25.2024

Question:
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or
right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D table First:
        #table = [[0] * n] * m
        table = [[0 for x in range(n)] for y in range(m)]
        # print(table)
        # Base Case
        for row in range(m):
            table[row][0] = 1
        for col in range(n):
            table[0][col] = 1

        for row in range(1, m):
            for col in range(1, n):
                # Compute Table
                table[row][col] = table[row - 1][col] + table[row][col - 1]
        return table[row][col]