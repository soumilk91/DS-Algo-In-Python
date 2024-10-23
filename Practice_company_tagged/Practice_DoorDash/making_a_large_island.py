"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.



Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
"""

from typing import *
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Directions for moving up, down, left, and right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Function to perform DFS and mark the island with a unique id
        def dfs(r, c, island_id):
            stack = [(r, c)]
            grid[r][c] = island_id
            island_size = 0

            while stack:
                cr, cc = stack.pop()
                island_size += 1
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = island_id
                        stack.append((nr, nc))
            return island_size

        # Step 1: Identify all islands and calculate their sizes
        island_id = 2  # Start labeling islands from 2 (since 1 and 0 are already used)
        island_sizes = {}

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = dfs(r, c, island_id)
                    island_sizes[island_id] = size
                    island_id += 1

        # If the grid is entirely 1's, return the size of the whole grid
        if len(island_sizes) == 0:
            return 1
        max_size = max(island_sizes.values())

        # Step 2: Try flipping each 0 to a 1 and check the island size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    # Check neighboring islands
                    seen_islands = set()
                    new_size = 1  # Starting size after flipping this 0 to 1

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            island_id = grid[nr][nc]
                            if island_id not in seen_islands:
                                seen_islands.add(island_id)
                                new_size += island_sizes[island_id]

                    max_size = max(max_size, new_size)

        return max_size
