"""
Author: Soumil Ramesh Kulkarni
Date: 02.21.2024

Question:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1

        # First put all the Prefix's in the result list
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # print(result)

        # Now use a while loop backwards and for
        # each index calculate the postfix
        postfix = 1
        temp = len(nums) - 1
        while temp >= 0:
            result[temp] *= postfix
            postfix *= nums[temp]
            temp -= 1

        return result
