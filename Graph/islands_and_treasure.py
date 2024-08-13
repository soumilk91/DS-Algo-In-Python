"""
Author: Soumil Kulkarni

Question:
You are given a
𝑚
×
𝑛
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Example:
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
"""

from collections import deque
from typing import *
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # Only have treasure points in the Queue for BFS and tarverse the graph while changing the values

        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque([])
        # Only add the Treasure locations to the Queue
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # Now BFS
        while queue:
            row, col, distance = queue.popleft()
            distance += 1
            for direction in directions:
                newR, newC = row + direction[0], col + direction[1]
                if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 2147483647:
                    grid[newR][newC] = distance
                    queue.append((newR, newC, distance))

