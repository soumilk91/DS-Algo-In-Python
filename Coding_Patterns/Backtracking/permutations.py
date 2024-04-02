"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

Question:
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""


class Solution:
    def permute_helper(self, nums, start_index, slate, result):
        # Base Case
        if start_index == len(nums):
            result.append(slate[:])
            return

        # Recursive Case
        for temp in range(start_index, len(nums)):
            nums[temp], nums[start_index] = nums[start_index], nums[temp]
            slate.append(nums[start_index])

            self.permute_helper(nums, start_index + 1, slate, result)

            slate.pop()

            nums[temp], nums[start_index] = nums[start_index], nums[temp]

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        index = 0
        self.permute_helper(nums, index, [], result)
        return result