"""
Author: Soumil Ramesh Kulkarni
Date: 08.14.2024

Question:
You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at
coordinate (r, c).

The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and
right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower.
Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list
where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

Example:
Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]

Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
"""

from typing import *
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])

        pacificQueue = deque([])
        atlanticQueue = deque([])

        for i in range(ROWS):
            pacificQueue.append((i, 0))
            atlanticQueue.append((i, COLS - 1))

        for i in range(COLS):
            pacificQueue.append((0, i))
            atlanticQueue.append((ROWS - 1, i))

        def bfs(queue):
            rechable = set()
            while queue:
                row, col = queue.popleft()
                rechable.add((row, col))
                for (x, y) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    newRow, newCol = row + x, col + y
                    if newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS:
                        continue
                    if (newRow, newCol) in rechable:
                        continue
                    if heights[newRow][newCol] < heights[row][col]:
                        continue
                    queue.append((newRow, newCol))
            return rechable

        pacific = bfs(pacificQueue)
        atlantic = bfs(atlanticQueue)
        return list(pacific.intersection(atlantic))