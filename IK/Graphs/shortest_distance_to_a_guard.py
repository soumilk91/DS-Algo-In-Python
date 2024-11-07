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
    if not grid:
        return grid

    ROWS, COLS = len(grid), len(grid[0])
    queue = deque()
    # Initialize the distance matrix with infinity for open spaces and -1 for walls
    distance = [[-1 if grid[r][c] == 'W' else float('inf') for c in range(COLS)] for r in range(ROWS)]

    # Enqueue all guards and set their distances to 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "G":
                queue.append((row, col))
                distance[row][col] = 0

    # Directions for up, down, left, right
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    # Perform BFS
    while queue:
        row, col = queue.popleft()
        currDistance = distance[row][col]

        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            if 0 <= newRow < ROWS and 0 <= newCol < COLS and grid[newRow][newCol] == "O":
                # If the current path offers a shorter distance, update it
                if distance[newRow][newCol] > currDistance + 1:
                    distance[newRow][newCol] = currDistance + 1
                    queue.append((newRow, newCol))

    # Replace 'inf' with -1 for cells that can't reach a guard
    for r in range(ROWS):
        for c in range(COLS):
            if distance[r][c] == float('inf'):
                distance[r][c] = -1

    return distance
