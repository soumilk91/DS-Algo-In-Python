"""
Link to the Problem: https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150

Author: Soumil Ramesh Kulkarni
Date: 02.19.2024

Question:
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping_dict = {}
        values = ""
        for index in range(len(s)):
            if s[index] not in mapping_dict:
                if t[index] not in values:
                    mapping_dict[s[index]] = t[index]
                    values += t[index]
                else:
                    return False
            else:
                if mapping_dict[s[index]] != t[index]:
                    return False
        return True 