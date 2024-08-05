"""
Author: Soumil Ramesh Kulkarni
Date: 05.11.2024

Question:
You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.
You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that
starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

Example 1:
Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).

Example 2:
Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)

Example 3:
Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
"""
from typing import *


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # dict for transition rule
        rules = {
            1: {0: 0, 3: 3},
            2: {1: 1, 2: 2},
            3: {0: 2, 1: 3},
            4: {1: 0, 3: 2},
            5: {0: 1, 2: 3},
            6: {2: 0, 3: 1},
        }

        # dict for update rule
        moves = {
            0: (0, 1),
            1: (-1, 0),
            2: (1, 0),
            3: (0, -1),
        }

        x, y = (0, 0)
        k = grid[0][0]
        d = list(rules[k].keys())
        d1, d2 = d[0], d[1]

        def walkMaze(x, y, d):
            visited = set([(x, y)])
            while True:
                if x < 0 or x >= m or y < 0 or y >= n:
                    return False

                k = grid[x][y]
                if d not in rules[k]:
                    return False

                if (x, y) == (m - 1, n - 1):
                    return True

                d = rules[k][d]
                x, y = (x + moves[d][0], y + moves[d][1])
                if (x, y) in visited:  # there is a loop
                    return False
                visited.add((x, y))

        return walkMaze(x, y, d1) or walkMaze(x, y, d2)
