"""
Author: Soumil Ramesh Kulkarni
Date: 05.07.2024

Question:
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.



Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""

from typing import *


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {}
        sum_val = 0
        max_len = 0
        for index, num in enumerate(nums):
            if num == 1:
                sum_val += 1
            else:
                sum_val -= 1
            if sum_val == 0:
                max_len = index + 1
            elif sum_val in map:
                max_len = max(max_len, index - map[sum_val])
            else:
                map[sum_val] = index
        return max_len
