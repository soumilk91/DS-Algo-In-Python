"""
Author: Soumil Ramesh Kulkarni
Date: 05.11.2024

Question:
Find the minimum number of die rolls necessary to reach the final cell of the given Snakes and Ladders board game.

Rules are as usual. Player starts from cell one, rolls a die and advances 1-6 (a random number of) steps at a time.
Should they land on a cell where a ladder starts, the player immediately climbs up that ladder. Similarly, having
landed on a cell with a snake’s mouth, the player goes down to the tail of that snake before they roll the die again.
Game ends when the player arrives at the last cell.

The function has two input arguments:

n, size of the board, and
moves, array of integers defining the snakes and ladders:
moves[i] = -1: no ladder or snake starts at i-th cell
moves[i] < i: snake from i down to moves[i]
moves[i] > i: ladder from i up to moves[i]
The indices and values in moves array are zero-based, for example moves[1] = 18 means there is a ladder from cell 2 up to cell 19.

Example One
{
"n": 20,
"moves": [-1, 18, -1, -1, -1, -1, -1, -1, 2, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1]
}
Output:

2
Example image

A board with 20 cells, two ladders 2->19 and 13->16, and a snake 9->3.

Note that the two-dimensional view is for our visual convenience only: there are really just 20 cells, one after another, linearly.

Having started from cell 1, the player rolls 1 and moves to cell 2. The ladder takes them from cell 2 to cell 19.
They don't roll the die again since they've already reached the final cell. The player reached the end of the board
in just one roll after climbing the ladder, that’s the fewest rolls possible.

Example Two
{
"n": 8,
"moves": [-1, -1, -1, -1, -1, -1, -1, -1]
}
Output:

2
Example two

A board with eight cells, no snakes and no ladders.

There are several ways to reach the last cell from the first cell in two rolls: 6+1, 5+2, 4+3, 3+4, 2+5, 1+6.
No way to reach it with any fewer rolls though.
"""


def minimum_number_of_rolls(n, moves):
    """
    Args:
     n(int32)
     moves(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    res = 0
    curr_pos = [0]
    visited = [False] * n

    while curr_pos:
        next_pos = []

        for cell in curr_pos:

            if cell == n - 1:
                return res

            for move in range(cell + 1, cell + 7):

                if move < n and not visited[move]:

                    visited[move] = True

                    if moves[move] != -1:

                        next_pos.append(moves[move])
                        visited[moves[move]] = True

                    else:
                        next_pos.append(move)

        res += 1
        curr_pos = next_pos

    return -1