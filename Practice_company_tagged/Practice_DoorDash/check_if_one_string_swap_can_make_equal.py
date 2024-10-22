"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.



Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
"""

from collections import defaultdict
from typing import *
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        s1_chars = defaultdict(int)
        s2_chars = defaultdict(int)
        for index in range(len(s1)):
            s1_chars[s1[index]] += 1
            s2_chars[s2[index]] += 1
        if s1_chars != s2_chars:
            return False

        index = 0
        changes = 0
        while index < len(s1):
            if s1[index] != s2[index]:
                changes += 1
            index += 1

        if changes != 2:
            return False
        return True
