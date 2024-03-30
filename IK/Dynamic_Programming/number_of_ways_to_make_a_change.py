"""
Author: Soumil Ramesh Kulkarni
Date: 03.29.2024

Question:
Given a variety of coin denominations existing in a currency system, find the total number of ways a given amount of
money can be expressed using coins in that currency system.

Assume infinite supply of coins of every denomination. Return answer modulo 1000000007.

Example
{
"coins ": [1, 2, 3],
"amount": 3
}
Output:

3
The three ways are:

Use the coin with denomination 1 three times.
Use the coin with denomination 3 once.
Use the coin with denomination 2 once and coin with denomination 1 once.

"""

def number_of_ways(coins, amount):
    """
    Args:
     coins(list_int32)
     amount(int32)
    Returns:
     int32
    """
    # Write your code here.
    dp = [0 for _ in range(amount + 1)]

    # (2) Initialize base cases
    dp[0] = 1

    # (3) Traversal direction
    # L -> R = dp[1] to dp[amount]
    # Subproblem F(amount) = coin + f(amount-coin)

    # (4) Populate table
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]

    return dp[amount] % 1000000007