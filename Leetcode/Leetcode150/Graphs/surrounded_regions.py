"""
Author: Soumil Ramesh Kulkarni
Date: 03.19.2024

Question:
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
"""

from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        ROWS = len(board)
        COLS = len(board[0])

        def disqualify_cells():
            queue = deque([])
            for row in range(ROWS):
                for col in range(COLS):
                    if (board[row][col] == "O") and (row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1):
                        board[row][col] = "E"
                        queue.append((row, col))

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                row, col = queue.popleft()
                for direction in directions:
                    newRow, newCol = row + direction[0], col + direction[1]
                    if 0 <= newRow < ROWS and 0 <= newCol < COLS and board[newRow][newCol] == "O":
                        board[newRow][newCol] = "E"
                        queue.append((newRow, newCol))

        disqualify_cells()
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "E":
                    board[row][col] = "O"