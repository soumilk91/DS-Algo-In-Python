"""
Author: Soumil Ramesh Kulkarni
Date: 03.21.2024

Question:
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sum = 0
        compare_dict = {0: 1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in compare_dict:
                result += compare_dict[prefix_sum - k]

            if prefix_sum not in compare_dict:
                compare_dict[prefix_sum] = 1
            else:
                compare_dict[prefix_sum] = compare_dict[prefix_sum] + 1
        return result