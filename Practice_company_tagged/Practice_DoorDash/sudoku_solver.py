"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

"""


class Solution:
    def solveSudoku(self, board):
        """
        Solves the Sudoku puzzle by filling empty cells in-place.
        """
        self.solve(board)

    def solve(self, board):
        # Try to find an empty cell
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    # Try placing each number from 1 to 9
                    for num in '123456789':
                        if self.isValid(board, i, j, num):
                            board[i][j] = num  # Place the number

                            # Recursively attempt to solve the rest of the board
                            if self.solve(board):
                                return True

                            # If the placement didn't lead to a solution, backtrack
                            board[i][j] = '.'

                    # If no number can be placed in this cell, return False
                    return False
        return True  # Puzzle is solved if there are no empty cells

    def isValid(self, board, row, col, num):
        """
        Checks if placing num in board[row][col] is valid based on Sudoku rules.
        """
        # Check if num is not in the current row, column, and 3x3 sub-box
        for i in range(9):
            if board[row][i] == num:  # Check row
                return False
            if board[i][col] == num:  # Check column
                return False
            # Check 3x3 sub-box
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True