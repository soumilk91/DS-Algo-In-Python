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
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.dia = [0] * 2

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            if row == col: self.dia[0] += 1
            if row + col == self.n - 1: self.dia[1] += 1
            if self.row[row] == self.n or self.col[col] == self.n or self.dia[0] == self.n or self.dia[
                1] == self.n: return 1
        else:
            self.row[row] -= 1
            self.col[col] -= 1
            if row == col: self.dia[0] -= 1
            if row + col == self.n - 1: self.dia[1] -= 1
            if self.row[row] == -self.n or self.col[col] == -self.n or self.dia[0] == -self.n or self.dia[
                1] == -self.n: return 2
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)