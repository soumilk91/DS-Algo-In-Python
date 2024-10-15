"""

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

from typing import *
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        targetFound = False
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                targetFound = True
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if not targetFound:
            return [-1, -1]
        starting = mid
        ending = mid
        while starting > 0 and nums[starting - 1] == target:
            starting -= 1
        while ending < len(nums) - 1 and nums[ending + 1] == target:
            ending += 1
        return [starting, ending]
