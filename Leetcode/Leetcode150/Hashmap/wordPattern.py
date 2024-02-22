"""
Author: Soumil Ramesh Kulkarni
Date: 02.20.2024

Question:
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.



Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(pattern) != len(s_list):
            return False
        compare_dict = {}
        for index in range(len(pattern)):
            if pattern[index] not in compare_dict:
                for j in compare_dict:
                    if compare_dict[j] == s_list[index]:
                        return False
                compare_dict[pattern[index]] = s_list[index]
            else:
                if compare_dict[pattern[index]] != s_list[index]:
                    return False
        return True

