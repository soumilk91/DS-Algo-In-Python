"""
Author: Soumil Kulkarni
Date: 08.14.2024

Question:
You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every second, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of seconds that must elapse until there are zero fresh fruits remaining.
If this state is impossible within the grid, return -1.

Example:
Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

Output: 4
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