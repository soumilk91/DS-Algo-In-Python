"""
Author: Soumil Ramesh Kulkarni
Date: 03.16.2024

Question:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""

from math import e, log


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = int(e ** (0.5 * log(x)))
        right = left + 1

        return left if right * right > x else right
