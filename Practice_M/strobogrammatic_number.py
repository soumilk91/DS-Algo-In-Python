"""
Question:
Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).



Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
"""

from typing import *
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        rotated_string_builder = []
        for c in reversed(num):
            if c not in rotated_digits:
                return False
            rotated_string_builder.append(rotated_digits[c])

        rotated_string = "".join(rotated_string_builder)
        return rotated_string == num