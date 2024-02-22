"""
Author: Soumil Ramesh Kulkarni
Date: 02.20.2024

Question:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start_s = 0
        start_t = 0
        while start_s < len(s) and start_t < len(t):
            if s[start_s] == t[start_t]:
                start_s += 1
                start_t += 1
            else:
                start_t += 1
        return start_s == len(s)
