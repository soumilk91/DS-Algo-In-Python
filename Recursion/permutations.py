"""
Author: Soumil Ramesh Kulkarni
Date: 01/17/2024

Question: Given a list of distinct integers, return all the possible permutations.
eg: input = [1,2,3]
Output = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
"""

from typing import *
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums, index, slate, result):
        # Base Case
        if index == len(nums):
            result.append(slate[:])
            return

        # Permute. Recursive Case
        for temp in range(index, len(nums)):
            nums[temp], nums[index] = nums[index], nums[temp]
            slate.append(nums[index])
            self.helper(nums, index + 1, slate, result)

            # Swap Again and Pop from Slate
            nums[temp], nums[index] = nums[index], nums[temp]
            slate.pop()
