"""
Question:

Given a two-dimensional matrix of 0s and 1s, find the number of islands.

An island is a group of connected 1s or a standalone 1. A cell in the matrix can be connected to up to 8 neighbors:
2 vertical, 2 horizontal and 4 diagonal.

Example
{
"matrix": [
[1, 1, 0, 0, 0],
[0, 1, 0, 0, 1],
[1, 0, 0, 1, 1],
[0, 0, 0, 0, 0],
[1, 0, 1, 0, 1]
]
}
Output:

5

"""

from collections import deque
def count_islands(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    if not matrix:
        return 0

    islands = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                islands += 1
                bfs(matrix, row, col)
    return islands


def bfs(matrix, row, col):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    # Use BFS for Traversal
    queue = deque([(row, col)])
    while queue:
        row, col = queue.popleft()
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] == 1:
            matrix[row][col] = 2
            for direction in directions:
                queue.append((row + direction[0], col + direction[1]))