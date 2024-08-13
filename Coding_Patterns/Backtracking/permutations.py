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

from typing import *
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        result = []
        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums, index, slate, result):
        # Base Case
        if index == len(nums):
            result.append(slate[:])
            return

        # Recursive Case
        # Swap
        for temp in range(index, len(nums)):
            nums[temp], nums[index] = nums[index], nums[temp]
            slate.append(nums[index])
            self.helper(nums, index + 1, slate, result)
            slate.pop()
            nums[temp], nums[index] = nums[index], nums[temp]

client = Solution()
print(client.permute([1,2,3]))