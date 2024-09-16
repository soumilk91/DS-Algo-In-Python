"""
Author: Soumil Ramesh Kulkarni
Date: 03.16.2024

Question:
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""
from collections import deque
from typing import *
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        time = 0
        fresh = 0
        rotten = deque([])

        # Only put rotten oranges in the queue while counting the fresh ones
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    rotten.append((row, col))

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while fresh > 0 and rotten:
            for i in range(len(rotten)):
                row, col = rotten.popleft()
                for direction in directions:
                    newRow, newCol = row + direction[0], col + direction[1]
                    if 0 <= newRow < ROWS and 0 <= newCol < COLS and grid[newRow][newCol] == 1:
                        fresh -= 1
                        grid[newRow][newCol] = 2
                        rotten.append((newRow, newCol))
            time += 1

        if fresh != 0:
            return -1
        return time
