"""
Author: Soumil Ramesh Kulkarni
Date: 03.25.2024

Question:
You are given an integer array coins representing coins of different denominations and an integer amount representing a
total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
"""

import math
from typing import *
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [math.inf] * (amount + 1)
        table[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                if i - coin >= 0:
                    table[i] = min(table[i], table[i - coin] + 1)

        return -1 if table[-1] == math.inf else table[-1]