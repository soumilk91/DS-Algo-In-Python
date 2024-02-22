"""
Author: Soumil Ramesh Kulkarni
Date: 02.21.2024

Question:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        elif nums[(len(nums) - 1)] < target:
            return len(nums)
        else:
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    return mid
            return start
