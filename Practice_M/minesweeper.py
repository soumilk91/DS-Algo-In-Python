"""
Author: Soumil Ramesh Kulkarni
Date: 04.15.2024

Question:
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

Example1:
Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

Example2:
Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
"""

from typing import *
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        ## RC ##
        ## APPROACH : DFS ##

        def adjacent_mines(i, j):
            mines = 0
            for x, y in directions:
                if 0 <= i + x < M and 0 <= j + y < N and board[i + x][j + y] == "M":
                    mines += 1
            return mines

        def dfs(i, j):

            # mark adjacent mine count at click position and return the board
            mines = adjacent_mines(i, j)
            if mines:
                board[i][j] = str(mines)
                return board

            # if no adjacent mines found then, do DFS
            board[i][j] = "B"

            for x, y in directions:
                if 0 <= i + x < M and 0 <= j + y < N and board[i + x][j + y] == "E":
                    dfs(i + x, j + y)
            return board

        if not board: return board
        M = len(board)
        N = len(board[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        # if click directly has mine, mark it as X and return
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        # if board has 'E' then check neighbors
        if board[click[0]][click[1]] == "E":
            return dfs(click[0], click[1])