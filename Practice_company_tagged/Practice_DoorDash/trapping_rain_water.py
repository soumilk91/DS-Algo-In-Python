"""
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map,
return the volume of water it can trap after raining.


Example 1:
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.

Example 2:
Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
"""

from typing import *
import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []

        # Add all boundary cells to the heap and mark them as visited
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        water_trapped = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        while min_heap:
            height, x, y = heapq.heappop(min_heap)

            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # Calculate the water trapped, if any
                    water_trapped += max(0, height - heightMap[nx][ny])

                    # Update the height of the neighboring cell to max(current height, neighbor height)
                    heapq.heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True

        return water_trapped
