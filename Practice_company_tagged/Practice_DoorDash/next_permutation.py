"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
"""

from typing import*
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Step 1: Find the pivot index where the first decreasing element from the end is located
        pivot_index = n - 2
        while pivot_index >= 0 and nums[pivot_index] >= nums[pivot_index + 1]:
            pivot_index -= 1

        if pivot_index >= 0:
            # Step 2: Find the rightmost element that is larger than nums[pivot_index]
            swap_index = n - 1
            while nums[swap_index] <= nums[pivot_index]:
                swap_index -= 1
            # Swap the pivot element with this element
            nums[pivot_index], nums[swap_index] = nums[swap_index], nums[pivot_index]

        # Step 3: Reverse the subarray to the right of the pivot_index
        left, right = pivot_index + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
