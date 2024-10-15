"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

from typing import *
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        index1 = 0
        index2 = 0
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] <= nums2[index2]:
                merged.append(nums1[index1])
                index1 += 1
            else:
                merged.append(nums2[index2])
                index2 += 1
        while index1 < len(nums1):
            merged.append(nums1[index1])
            index1 += 1

        while index2 < len(nums2):
            merged.append(nums2[index2])
            index2 += 1

        mid = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            return merged[mid]
