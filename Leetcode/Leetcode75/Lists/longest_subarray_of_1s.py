"""
Author: Soumil Ramesh Kulkarni
Date: 03.16.2024

Question:
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)  # The size of the input array

        left = 0  # The left pointer of the sliding window
        zeros = 0  # Number of zeroes encountered
        ans = 0  # Maximum length of the subarray

        for right in range(n):
            if nums[right] == 0:
                zeros += 1  # Increment the count of zeroes

            # Adjust the window to maintain at most one zero in the subarray
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1  # Decrement the count of zeroes
                left += 1  # Move the left pointer to the right

            # Calculate the length of the current subarray and update the maximum length
            ans = max(ans, right - left + 1 - zeros)

        # If the entire array is the subarray, return the size minus one; otherwise, return the maximum length
        return ans - 1 if ans == n else ans