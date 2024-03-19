"""
Author: Soumil Ramesh Kulkarni
Date: 03.19.2024

Question:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return -1
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        # Already sorted array. Just return the first element
        if nums[right] > nums[left]:
            return nums[left]

        # Binary Search
        while left <= right:
            mid = left + (right - left) // 2
            # If mid element is greater than the next element then next element is smallest
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # If mid element is lesser than its previous element, mid is smallest
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            # If mid is greater than 0th element, smallest value is somewhere to the right
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                # if nums[0] > nums[mid], smallest is somewhere to the left
                right = mid - 1