"""
Author: Soumil Ramesh Kulkarni
Date: 03.25.2024

Question:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        table = [0] * (n + 1)
        table[1] = 1
        table[2] = 2
        for i in range(3, n + 1):
            table[i] = table[i - 1] + table[i - 2]
        return table[n]