"""
Author: Soumil Ramesh Kulkarni
Date: 03.22.2024

Question:
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
0 if there is no winner after the move,
1 if player 1 is the winner after the move, or
2 if player 2 is the winner after the move.


Example 1:

Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

"""


class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)]
        self.ROWS = len(self.board)
        self.COLS = len(self.board[0])
        self.n = n

    def checkResult(self, row, col, player):
        if self.checkRow(row, col, player):
            return True
        if self.checkCol(row, col, player):
            return True
        if self.checkDigonal(row, col, player):
            return True
        return False

    def checkRow(self, row, col, player):
        for c in range(self.COLS):
            if self.board[row][c] != player:
                return False
        return True

    def checkDigonal(self, row, col, player):
        # check main diagonal only if (row, col) is on it
        if row == col:
            for i in range(self.n):
                if self.board[i][i] != player:
                    break
            else:
                return True  # all matched

        # check anti-diagonal only if (row, col) is on it
        if row + col == self.n - 1:
            for i in range(self.n):
                if self.board[i][self.n - 1 - i] != player:
                    break
            else:
                return True  # all matched

        return False

    def checkCol(self, row, col, player):
        for r in range(self.ROWS):
            if self.board[r][col] != player:
                return False
        return True

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if self.checkResult(row, col, player):
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)