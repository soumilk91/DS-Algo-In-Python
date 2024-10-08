"""
Author: Soumil Ramesh Kulkarni
Date: 03.25.2024

Question:
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

from typing import *
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums, index, slate, result):
        # Base Case
        if index == len(nums):
            result.append(slate[:])
            return

        # Recursive Cases
        # Include
        slate.append(nums[index])
        self.helper(nums, index + 1, slate, result)
        slate.pop()

        # Exclude
        self.helper(nums, index + 1, slate, result)
