"""
Author: Soumil Ramesh Kulkarni
Date: 05.12.2024

Question:
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.



Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
"""
from typing import *
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        # find the common 1-bits
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift