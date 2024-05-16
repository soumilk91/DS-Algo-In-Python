"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:
Consider a row of n coins of values v1, . . . , vn. We play a game against an opponent by alternating turns.
In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and
receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first.

Assume full competency by both players.

Example
{
"v": [8, 15, 3, 7]
}
Output:

22
Player 1 can start two different ways: either picking 8 or picking 7. Depending on the choice they make, the end reward
will be different. We want to find the maximum reward player 1 can collect.

Case one: Player 1 starts by picking 8.
Remaining v = [15, 3, 7].
The opponent will have two choices: pick either 15 or 7. They would always pick 15 to maximize their own amount.
Remaining v = [3, 7].
Player 1 will have two choices: pick either 3 or 7.
Player 1 would always pick 7 to maximize their own amount.
Hence in this case player 1 can get a maximum of 8 + 7 = 15.
(This is a greedy strategy, picking the highest at every step.)

Case two: Player 1 starts by picking 7.
Remaining v = [8, 15, 3].
Opponent will have two choices, either pick 8 or 3.
The opponent would pick 8 to maximize their own amount. (If they pick 3 at this step, the answer will be the same though.)
Remaining v = [15, 3].
Player 1 will have two choices, either pick 15 or 3.
Player 1 would always pick 15.
Hence in this case player 1 can get a maximum of 7 + 15 = 22.

Given these two strategies, we want 22 as the answer, and not 15.
"""

def max_win(v):
    n = len(v)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = v[i]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            dp[i][j] = max(v[i] - dp[i+1][j], v[j] - dp[i][j-1])
    diff = dp[0][n-1]
    return (sum(v) - diff)//2 + diff