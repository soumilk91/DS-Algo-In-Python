"""
Author: Soumil Ramesh Kulkarni
Date: 03.30.2024

Question:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        compare_dict = {}
        for i in nums:
            if i not in compare_dict:
                compare_dict[i] = 1
            else:
                compare_dict[i] += 1
                if compare_dict[i] >= 2:
                    return True
        return False