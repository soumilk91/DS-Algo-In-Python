"""
Question:

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.



Example 1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
"""

from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        queue = deque([])
        # Only append Gates
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    queue.append((row, col))
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            x, y = queue.popleft()
            distance = rooms[x][y] + 1
            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                if 0 <= newX < len(rooms) and 0 <= newY < len(rooms[0]) and rooms[newX][newY] == 2147483647:
                    rooms[newX][newY] = distance
                    queue.append((newX, newY))
