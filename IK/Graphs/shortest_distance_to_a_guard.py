"""
Author: Soumil Ramesh Kulkanrni
Date: 05.11.2024

Question:
You are given a two-dimensional character grid n by m. Each element of the grid is either a Guard,
an Open space or a Wall. A guard can move up, down, left or right in the Open space. They cannot move on Walls.

For every Open space cell, find the shortest distance to the nearest guard.

Example One
{
"grid": [
["O", "O", "O", "O", "G"],
["O", "W", "W", "O", "O"],
["O", "O", "O", "W", "O"],
["G", "W", "W", "W", "O"],
["O", "O", "O", "O", "G"]
]
Output:

[
[3,  3,  2,  1,  0],
[2, -1, -1,  2,  1],
[1,  2,  3, -1,  2],
[0, -1, -1, -1,  1],
[1,  2,  2,  1,  0]
]
All Guard cells have zero distance to the nearest guard.
We consider the distance from the Wall cells to the nearest guard be -1.
For other (Open space) cells, we calculated the distance.

Example Two
{
"grid": [
["G", "W", "O", "W", "G"]
]
}
Output:

[
[0, -1, -1, -1, 0]
]
The Open space cell in the middle is unreachable for guards, so the distance is considered to be -1.
"""

from collections import deque
def find_shortest_distance_from_a_guard(grid):
    """
    Args:
     grid(list_list_char)
    Returns:
     list_list_int32
    """
    # Write your code here.
    rmax = len(grid)
    cmax = len(grid[0])

    def bfs(queue):
        nei = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            (ci, cj, level) = queue.popleft()
            for di, dj in nei:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= rmax:
                    continue
                if nj < 0 or nj >= cmax:
                    continue
                if grid[ni][nj] == 'O':
                    grid[ni][nj] = level + 1
                    queue.append((ni, nj, level + 1))
        return -1

    queue = deque()
    for i in range(rmax):
        for j in range(cmax):
            if grid[i][j] == 'W':
                grid[i][j] = -1
            elif grid[i][j] == 'G':
                grid[i][j] = 0
                queue.append((i, j, 0))
    bfs(queue)

    for i in range(rmax):
        for j in range(cmax):
            if grid[i][j] == 'O':
                grid[i][j] = -1
    return grid
