"""
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

Example1:
Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
Output: 3
Explanation: It takes 3 steps to reach the food.

Example2:
Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
Output: -1
Explanation: It is not possible to reach the food.

Example3:
Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
Output: 6
Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.
"""

from typing import *
from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque([])
        visited = set()
        # Put the starting point in the Queue along with the distance
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "*":
                    queue.append((row, col, 0))
                    visited.add((row, col))
                    break

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            row, col, currDistance = queue.popleft()
            if grid[row][col] == "#":
                return currDistance
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                if 0 <= newRow < ROWS and 0 <= newCol < COLS and (newRow, newCol) not in visited and grid[newRow][
                    newCol] != 'X':
                    visited.add((newRow, newCol))
                    queue.append((newRow, newCol, currDistance + 1))
        return -1

