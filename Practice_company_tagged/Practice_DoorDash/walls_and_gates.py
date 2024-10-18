"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the
distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example 1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],
[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
"""

from collections import deque
from typing import *
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        1) Traverse all the cells and only put all the gates in a queue
        2) from the queue, traverse all the possible cells and update the distance where ever possible
        """
        ROWS = len(rooms)
        COLS = len(rooms[0])
        queue = deque([])
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:  # IF Gate Found, record it
                    queue.append((row, col, 0))  # Row, Col, Current Distance
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            row, col, current_distance = queue.popleft()
            for direction in directions:
                newRow = direction[0] + row
                newCol = direction[1] + col
                newDistance = current_distance + 1
                if 0 <= newRow < ROWS and 0 <= newCol < COLS and rooms[newRow][newCol] == 2147483647:
                    rooms[newRow][newCol] = newDistance
                    queue.append((newRow, newCol, newDistance))

