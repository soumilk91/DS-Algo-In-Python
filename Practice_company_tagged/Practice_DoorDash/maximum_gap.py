"""
Given an integer array nums, return the maximum difference between two successive elements in its sorted form.
If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.



Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
"""

from typing import *
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        min_num, max_num = min(nums), max(nums)
        if min_num == max_num:
            return 0
        n = len(nums)

        # Calculate bucket size and count
        bucket_size = max(1, (max_num - min_num) // (n - 1))
        bucket_count = (max_num - min_num) // bucket_size + 1

        # Initialize buckets
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

        # Distribute numbers into buckets
        for num in nums:
            idx = (num - min_num) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)

        # Calculate maximum gap
        max_gap = 0
        previous_max = min_num
        for bucket_min, bucket_max in buckets:
            if bucket_min == float('inf'):
                continue
            max_gap = max(max_gap, bucket_min - previous_max)
            previous_max = bucket_max

        return max_gap
