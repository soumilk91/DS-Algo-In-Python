"""
Author: Soumil Ramesh Kulkarni
Date: 03.30.2024

Question:
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

"""
# Time: O(N), Space: O(N)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        compare_dict = {}
        for num in nums:
            if num not in compare_dict:
                compare_dict[num] = 1
            else:
                return num
        return -1

# Time: O(NlogN), Space: O(N)
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums) + 1):
            if nums[i - 1] == nums[i]:
                return nums[i]
        return -1
