"""
Author: Soumil Ramesh Kulkarni
Date: 01/19/2024

Question:
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.



Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        compare_dict = {}
        for item in arr:
            if item in compare_dict:
                compare_dict[item] += 1
            else:
                compare_dict[item] = 1
        occurences = compare_dict.values()
        compare_dict1 = {}
        for value in occurences:
            if value in compare_dict1:
                return False
            else:
                compare_dict1[value] = 1
        return True
