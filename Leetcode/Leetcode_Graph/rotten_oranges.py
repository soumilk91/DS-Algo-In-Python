"""
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
        fresh = 0
        queue = deque([])
        minutes = 0

        # Only insert the rotten fruits in the queue while counting the fresh Fruits
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))

        # Now a BFS on the Graph ...
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while fresh > 0 and queue:
            # For loop on the current set of rotten Fruits
            for i in range(len(queue)):
                row, col = queue.popleft()
                for direction in directions:
                    newR, newC = row + direction[0], col + direction[1]
                    if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 1:
                        fresh -= 1
                        grid[newR][newC] = 2
                        queue.append((newR, newC))
            minutes += 1

        if fresh != 0:
            return -1
        return minutes