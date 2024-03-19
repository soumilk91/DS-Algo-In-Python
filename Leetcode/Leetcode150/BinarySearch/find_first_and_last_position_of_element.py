"""
Author: Soumil Ramesh Kulkarni
Date: 03.19.2024

Question:
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""


class Solution:
    def find_bound(self, nums, target, isFirst):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                if isFirst:
                    # This means we found the lower bound
                    if mid == start or nums[mid - 1] < target:
                        return mid
                    else:
                        end = mid - 1
                else:
                    # This means we found the upper bound
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    else:
                        start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.find_bound(nums, target, True)
        if lower_bound == -1:
            return [-1, -1]

        upper_bound = self.find_bound(nums, target, False)

        return [lower_bound, upper_bound]