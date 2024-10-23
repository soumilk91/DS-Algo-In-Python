"""
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance.
You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to
the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example1:
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.

Example 2:
Input: grid = [[1,0]]
Output: 1

Example 3:
Input: grid = [[1]]
Output: -1

"""

from collections import deque
from typing import *
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        total_distances = [[0] * cols for _ in range(rows)]
        reachable_count = [[0] * cols for _ in range(rows)]

        buildings = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    buildings.append((r, c))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(building_r, building_c):
            visited = [[False] * cols for _ in range(rows)]
            queue = deque([(building_r, building_c, 0)])  # (row, col, distance)
            visited[building_r][building_c] = True

            while queue:
                r, c, dist = queue.popleft()

                # Traverse all 4 possible directions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        if grid[nr][nc] == 0:
                            # Update total distance and reachable count
                            total_distances[nr][nc] += dist + 1
                            reachable_count[nr][nc] += 1
                            queue.append((nr, nc, dist + 1))
                        visited[nr][nc] = True

        # Perform BFS from each building
        for br, bc in buildings:
            bfs(br, bc)

        # Find the minimum distance for all lands that can be reached by all buildings
        min_distance = float('inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and reachable_count[r][c] == len(buildings):
                    min_distance = min(min_distance, total_distances[r][c])

        return min_distance if min_distance != float('inf') else -1
