"""
Question:

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

"""

from typing import *
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redPointer = 0
        runner = 0
        bluePointer = len(nums) - 1
        while runner <= bluePointer:
            if nums[runner] == 0:  # Red
                # Swap
                nums[redPointer], nums[runner] = nums[runner], nums[redPointer]
                redPointer += 1
                runner += 1
            elif nums[runner] == 2:  # Blue
                # Swap
                nums[bluePointer], nums[runner] = nums[runner], nums[bluePointer]
                bluePointer -= 1
            else:
                runner += 1
