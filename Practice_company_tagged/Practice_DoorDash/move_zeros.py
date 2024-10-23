"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

from typing import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        runner = 0
        index = 0
        while runner < len(nums):
            if nums[runner] != 0:
                nums[runner], nums[index] = nums[index], nums[runner]
                runner += 1
                index += 1
            else:
                runner += 1

