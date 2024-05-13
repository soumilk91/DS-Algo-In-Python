"""
Author: Soumil Ramesh Kulkarni
Date: 05.12.2024

Question:
Given an integer array nums where every element appears three times except for one,
which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
"""
from typing import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        for key in freq:
            if freq[key] == 1:
                return key