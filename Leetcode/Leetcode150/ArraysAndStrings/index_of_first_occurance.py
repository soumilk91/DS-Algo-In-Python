"""
Author: Soumil Ramesh Kulkarni
Date: 02.20.2024

Question:
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return_index = - 1
        for index in range(len(haystack)):
            if haystack[index] == needle[0]:
                temp_index = index
                compare_True = True
                for i in range(len(needle)):
                    if temp_index < len(haystack) and haystack[temp_index] == needle[i]:
                        temp_index += 1
                    else:
                        compare_True = False
                if compare_True:
                    return index
            else:
                continue
        return return_index
