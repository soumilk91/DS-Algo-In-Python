"""
Author: Soumil Ramesh Kulkarni
Date: 05.21.2024

Question:
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.



Example 1:

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:

Input: s = ["a"]
Output: ["a"]

"""

from typing import *
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Reverse the Entire String
        self.reverse(s, 0, len(s) - 1)
        # Reverse Each Word in the String
        self.reverse_eachword(s)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverse_eachword(self, s):
        start = 0
        n = len(s)
        end = 0
        while start < n:
            while end < n and s[end] != ' ':
                end += 1
            self.reverse(s, start, end - 1)
            start = end + 1
            end += 1