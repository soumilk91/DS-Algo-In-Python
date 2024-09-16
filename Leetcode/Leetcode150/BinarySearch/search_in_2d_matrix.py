"""
Author: Soumil Ramesh Kulkarni
Date: 03.19.2024

Question:
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

from typing import *
class Solution:
    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            if row[0] <= target <= row[len(row) - 1]:
                return self.binarySearch(row, target)

        return False