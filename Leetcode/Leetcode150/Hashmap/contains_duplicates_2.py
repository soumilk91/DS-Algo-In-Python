"""
Author: Soumil Ramesh Kulkarni
Date: 02.20.2024

Question:
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3]
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        compare_dict = {}
        for index, value in enumerate(nums):
            if value in compare_dict and abs(index - compare_dict[value]) <= k:
                return True
            else:
                compare_dict[value] = index
        return False


