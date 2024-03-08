"""
Author: Soumil Ramesh Kulkarni
Date: 03.06.2024

Question:
You are given a chessboard with rows rows and cols columns and a knight - that moves like in normal chess - located at the start_row-th row and start_col-th column. The knight needs to reach the position at the end_row-th row and end_col-th column.

Find minimum number of moves that knight needs to make to get from starting position to ending position.

start_row, start_col, end_row and end_col are all zero-indexed.

Example
{
"rows": 5,
"cols": 5,
"start_row": 0,
"start_col": 0,
"end_row": 4,
"end_col": 1
}
Output:

3
3 moves to reach from (0, 0) to (4, 1):
(0, 0) → (1, 2) → (3, 3) → (4, 1).
"""

"""
Asymptotic complexity in terms of number of rows `n` and number of columns `m` in the chessboard:
* Time: O(n * m).
* Auxiliary space: O(n * m).
* Total space: O(n * m).
"""

from collections import deque

DIRECTIONS = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    def get_neighbors(r, c):
        neighbors = []
        for dr, dc in DIRECTIONS:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < rows and 0 <= new_c < cols:
                neighbors.append((new_r, new_c))

        return neighbors

    start_cell = start_row, start_col

    # visited set to keep track of visited cells
    visited = {start_cell}

    # make a queue with cell and number of moves to get to that cell
    q = deque([(start_cell, 0)])

    while q:
        cell, count = q.popleft()
        if cell == (end_row, end_col):
            return count

        # using * operator to convert tuple into 2 arguments as get_neighbors function expects
        for new_cell in get_neighbors(*cell):
            if new_cell not in visited:
                q.append((new_cell, count + 1))
                visited.add(new_cell)

    return -1