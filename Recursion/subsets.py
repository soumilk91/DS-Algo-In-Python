"""
Author: Soumil Ramesh Kulkarni
Date: 01/17/2024

Question: Given a set of distinct integers, return all possible subsets ... No duplicates

The only question at each level of the recursive tree we need to ask is INCLUDE / EXCLUDE
eg: Input = [1,2,3]
Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
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

