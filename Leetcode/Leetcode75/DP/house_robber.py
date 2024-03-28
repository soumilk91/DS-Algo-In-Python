"""
Author: Soumil Ramesh Kulkarni
Date: 03.26.2024

Question:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # Base Cases when only 1 or 2 houses are present
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # Initialize
        table = [-1] * n
        table[0] = nums[0]
        table[1] = max(nums[0], nums[1])

        for i in range(2, n):
            table[i] = max(table[i - 1], table[i - 2] + nums[i])
        return table[n - 1]