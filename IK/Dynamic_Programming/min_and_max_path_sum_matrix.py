"""
Author: Soumil Ramesh Kulkarni
Date: 03.25.2024

Question:
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

"""


class Solution:
    def maxPathSum(self, grid: List[List[int]]) -> int:
        table = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        # print(table)
        # Initialize
        table[0][0] = grid[0][0]
        # print(table)
        for row in range(1, len(grid)):
            table[row][0] = table[row - 1][0] + grid[row][0]

        for column in range(1, len(grid[0])):
            table[0][column] = table[0][column - 1] + grid[0][column]
        # print(table)
        # Now fill the other blank items
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                table[row][col] = grid[row][col] + max(table[row - 1][col], table[row][col - 1])
        return table[len(grid) - 1][len(grid[0]) - 1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        table = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        # print(table)
        # Initialize
        table[0][0] = grid[0][0]
        # print(table)
        for row in range(1, len(grid)):
            table[row][0] = table[row - 1][0] + grid[row][0]

        for column in range(1, len(grid[0])):
            table[0][column] = table[0][column - 1] + grid[0][column]
        # print(table)
        # Now fill the other blank items
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                table[row][col] = grid[row][col] + min(table[row - 1][col], table[row][col - 1])
        return table[len(grid) - 1][len(grid[0]) - 1]

