"""
Link to Question: https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150
Author: Soumil Ramesh Kulkarni
Date: 02.20.2024

Question:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        compare_dict = {}
        for i in s:
            if i not in compare_dict:
                compare_dict[i] = 1
            else:
                compare_dict[i] += 1

        for j in t:
            if j not in compare_dict:
                return False
            else:
                compare_dict[j] -= 1
                if compare_dict[j] == 0:
                    del compare_dict[j]

        if len(compare_dict) == 0:
            return True
        else:
            return False
