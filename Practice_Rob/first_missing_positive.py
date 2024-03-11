"""
Author: Soumil Ramesh Kulkarni
Date: 03.02.2024

Question:
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2    is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Perform a Cyclic Sort Operation
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Basic For loop to find the first positive missing integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
