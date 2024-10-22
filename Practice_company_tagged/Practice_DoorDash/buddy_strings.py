"""
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
"""

from typing import *
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        # check same length
        if len(A) != len(B):
            return False

        # if strings are equal - check if there is a double to swap
        if A == B:
            if len(A) - len(set(A)) >= 1:
                return True
            return False

        # count differences between strings
        diff = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False

        # not exactly two differences
        if len(diff) != 2:
            return False

        # check if can be swapped
        if A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
            return True

        return False