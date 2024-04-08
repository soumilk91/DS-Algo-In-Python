"""
Author: Soumil Ramsh Kulkarni
Date: 02.20.2024

Question:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        compare_dict = {}
        for i in strs:
            if ''.join(sorted(i)) not in compare_dict:
                compare_dict[''.join(sorted(i))] = [i]
            else:
                compare_dict[''.join(sorted(i))].append(i)
        return compare_dict.values()
