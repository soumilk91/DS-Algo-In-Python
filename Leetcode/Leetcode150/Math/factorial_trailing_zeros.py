"""
Author: Soumil Ramesh Kulkarni
Date: 03.16.2024

Question:
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
"""


class Solution:
    def factorial(self, num):
        if num == 1:
            return 1
        return num * self.factorial(num - 1)

    def trailingZeroes(self, n: int) -> int:
        if n < 1:
            return 0
        fact_n = self.factorial(n)
        trailing_zeros = 0
        # print(fact_n)
        while fact_n % 10 == 0:
            trailing_zeros += 1
            fact_n = fact_n // 10
        return trailing_zeros