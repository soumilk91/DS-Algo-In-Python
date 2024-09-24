"""
Question:

Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

"""

from typing import *
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums, index, slate, result):
        # Base Case
        if index == len(nums):
            temp = tuple(sorted(slate[:]))
            if temp not in result:
                result.add(temp)
            return

        # Recursive Cases
        # Include
        slate.append(nums[index])
        self.helper(nums, index + 1, slate, result)
        slate.pop()

        # Exclude
        self.helper(nums, index + 1, slate, result)
