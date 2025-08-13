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
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to group duplicates
        result = []
        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums, index, slate, result):
        result.append(slate[:])  # Always add current subset

        for i in range(index, len(nums)):
            # Skip duplicates in the same recursive level
            if i > index and nums[i] == nums[i - 1]:
                continue
            slate.append(nums[i])
            self.helper(nums, i + 1, slate, result)
            slate.pop()

