"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

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


class Solution:
    def subset_helper(self, nums, start_index, slate, result):
        # Base Case
        if start_index == len(nums):
            result.append(slate[:])
            return
        # Recursive Case
        # Include
        slate.append(nums[start_index])
        self.subset_helper(nums, start_index + 1, slate, result)
        slate.pop()

        # Exclude
        self.subset_helper(nums, start_index + 1, slate, result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.subset_helper(nums, 0, [], result)
        return result