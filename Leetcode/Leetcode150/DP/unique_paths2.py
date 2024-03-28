"""
Author: Soumil Ramesh Kulkarni
Date: 03.26.2024

Question:
ou are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right
at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square
that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # print(obstacleGrid)
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # Initialize a table for calculations
        table = [[0 for j in range(n)] for i in range(m)]
        # Base Case when the first grid itself is an obstacle
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            table[0][0] = 1

        # Now initialize the table values.
        for row in range(m):
            if obstacleGrid[row][0] == 1:
                break
            table[row][0] = 1

        for col in range(n):
            if obstacleGrid[0][col] == 1:
                break
            table[0][col] = 1

        # Recursive Case to calculate the number of paths
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 1:
                    table[row][col] = 0
                else:
                    table[row][col] = table[row - 1][col] + table[row][col - 1]

        # Return the value in the last gird item of the table
        return table[m - 1][n - 1]